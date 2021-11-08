# Releasing TuDeT

1. Update the data in `raw/` running
   ```shell
   cldfbench download cldfbench_tudet.py
   ```
2. Re-create the CLDF data running
   ```shell
   cldfbench makecldf --with-cldfreadme cldfbench_tudet.py --glottolog-version v4.4
   ```
3. Make sure the CLDF is valid:
   ```shell
   pytest 
   ```
4. Create metadata for Zenodo:
   ```shell
   cldfbench zenodo cldfbench_tudet.py --communities tular
   ```
5. Create the release commit:
   ```shell
   git commit -a -m "release <VERSION>"
   ```
6. Create a release tag:
   ```
   git tag -a v<VERSION> -m"<VERSION> release"
   ```
7. Create a release from this tag on https://github.com/tupian-language-resources/tudet/releases
8. Verify that data and metadata has been picked up by Zenodo correctly,
   and copy the citation information into the GitHub release description.
