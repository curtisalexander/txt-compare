# txt-compare

Simple comparison of two text files.  Checks for the following:

* duplicates
* intersection between files
* union of files
* set differences between files


## Example


```sh
txt-compare.py --file1 test/txt1 --file2 test/txt2
```


## Requirements

* [click](click.pocoo.org)

```sh
conda install click
```