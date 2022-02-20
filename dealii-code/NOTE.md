---
title: Error Handling
---

## expand_instantiations error

```bash
./expand_instantiations template-arguments < inst/operator.inst.in

...
Invalid instantiation list: missing 'for'
```

```json
{
  "directory": "/mnt/e/ubuntu2004/dealii/build/cmake/scripts",
  "command": "/bin/g++-9  -DBOOST_NO_AUTO_PTR    -pedantic -fPIC -Wall -Wextra -Woverloaded-virtual -Wpointer-arith -Wsign-compare -Wsuggest-override -Wswitch -Wsynth -Wwrite-strings -Wno-placement-new -Wno-deprecated-declarations -Wno-literal-suffix -Wno-psabi -Wno-class-memaccess -fopenmp-simd -Wno-unused-local-typedefs -o CMakeFiles/expand_instantiations_exe.dir/expand_instantiations.cc.o -c /mnt/e/ubuntu2004/dealii/cmake/scripts/expand_instantiations.cc",
  "file": "/mnt/e/ubuntu2004/dealii/cmake/scripts/expand_instantiations.cc"
}
```

We run into a bug when compiling expand_instantiations with -fuse-ld=gold -pthreads, see <https://github.com/dealii/dealii/issues/1798> work around this by stripping -fuse-ld=gold out of the build flags for the script. This does little harm because linking this one file is so exceedingly cheap that there is no speed difference between using gold or the old BFD ld linker.
If we are on a system where -fuse-ld=gold simply isn't part of the linker flag, filtering this one command out of the list of flags does not harm either.

expand_instantiations を -fuse-ld=gold -pthreads でコンパイルするときにバグに遭遇します。<https://github.com/dealii/dealii/issues/1798>を参照してください。この1つのファイルのリンクは非常に安価なので、goldと古いBFD ldリンカのどちらを使っても速度の差がないので、これはほとんど害はありません。
もし -fuse-ld=gold がリンカフラグの一部になっていないシステムでは、このコマンドをフラグのリストから除外しても害はありません。

```c++
/* ======================== auxiliary functions ================= */

// Return whether or not one string starts with a given prefix
bool
has_prefix(const std::string &base, const std::string &prefix)
{
  if (prefix.size() > base.size())
    return false;
  else
    return std::equal(prefix.begin(), prefix.end(), base.begin());
}

// read the whole file specified by the stream given as argument into a string
// for simpler parsing, and return it
std::string
read_whole_file(std::istream &in)
{
  std::string whole_file;
  while (in)
    {
      std::string line;
      getline(in, line);

      whole_file += remove_comments(line);
      whole_file += '\n';
    }
  // substitute tabs by spaces
  std::replace(whole_file.begin(), whole_file.end(), '\t', ' ');
  // substitute multiple spaces by single ones
  std::size_t position = 0;
  while ((position = whole_file.find("  ", position)) != std::string::npos)
    whole_file.replace(position, 2, 1, ' ');

  return whole_file;
}

  std::string whole_file = read_whole_file(std::cin);

  // process entries of the form
  //   for (X:Y; A:B) { INST }
  while (whole_file.size() != 0)
    {
      skip_space(whole_file);
      if (!has_prefix(whole_file, "for"))
        {
          std::cerr << "Invalid instantiation list: missing 'for'" << std::endl;
          std::exit(1);
        }
    }
```

```bash
for (VEC : VECTOR_TYPES)
  {
    template class OutputOperator<VEC>;
    template class Newton<VEC>;
    template class ThetaTimestepping<VEC>;
  }
```
