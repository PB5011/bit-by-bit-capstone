rm -rf ../docs
rm -rf _build/*


# temporarily move index so it doesn't get deleted
mv index.rst index.tmp
rm ./*.rst
mv index.tmp index.rst

make clean
sphinx-apidoc -o . ..
make html

mkdir ../docs
mv _build/html/* ../docs/
touch ../docs/.nojekyll

echo "no jekyll" >> ../docs/.nojekyll
