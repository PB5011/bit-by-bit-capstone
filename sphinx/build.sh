rm -rf ../docs
rm -rf _build/*

sphinx-apidoc -o . ..
make html

mkdir ../docs
mv _build/html/* ../docs/
