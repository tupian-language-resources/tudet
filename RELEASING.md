# Releasing TuDeT

1. Update the data in `raw/` running
   ```shell
   cldfbench download cldfbench_tudet.py
   ```
2. Re-create the CLDF data running
   ```shell
   cldfbench makecldf cldfbench_tudet.py
   ```
3. Make sure the CLDF is valid:
   ```shell
   pytest 
   ```
4. Create metadata for Zenodo:
   ```shell
   cldfbench zenodo cldfbench_tudet.py
   ```

