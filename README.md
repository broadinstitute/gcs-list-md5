## List GCS objects with MD5 checksums

This repo provides a short script to list objects in a Google Cloud Storage bucket,
together with their MD5 checksums.

It prints the results as a JSON object.

Example usage:
```py
./gcs_md5.py example-bucket > ~/Downloads/example-bucket.json
```
