from db import DB
import os
import frontmatter
import wget

MAXIMUM_DATASETS = 5
def main():
    db = DB()
    db.connect()
    db.import_census_tracts()
    # find geojson resource urls
    cwd = os.getcwd()
    md_datasets_path = os.path.join(cwd, "..", "_datasets")
    i = 0
    for md_dataset_filename in os.listdir(md_datasets_path):
        if i > MAXIMUM_DATASETS:
            break
        md_dataset_path = os.path.join(md_datasets_path, md_dataset_filename)
        if os.path.isfile(md_dataset_path):
            try:
                md_dataset = frontmatter.load(md_dataset_path)
                resources = md_dataset.metadata.get("resources",[])
                resource_table_names = []
                for resource in resources:
                    if resource.get("format") == "GeoJSON":
                        resource_name = resource.get("name")
                        resource_path = (
                            f"working_files/{md_dataset_filename}-{resource_name}.geojson"
                        )
                        resource_url = resource.get("url")
                        if not os.path.exists(resource_path):
                            print(f"Downloading {resource_url} to {resource_path}...")
                            wget.download(resource_url, resource_path)
                            print("\nDownload complete.")
                        else:
                            print(
                                f"File {resource_path} already exists. Skipping download."
                            )
                        resource_table_name = md_dataset_filename.removesuffix('.md')+f"-{i}"
                        resource_table_names.append(resource_table_name)
                        db.prepare_datasets_table(resource_table_name)
                        db.import_dataset(resource_path, resource_table_name)
                        i = i+1
                if len(resource_table_names) > 0:
                    census_tracts = db.derive_census_tracts_from_datasets(resource_table_names)
                    print("Writing administrative boundary info into markdown file...")
                    md_dataset.metadata["census_tracts"] = census_tracts
                    frontmatter.dump(md_dataset, md_dataset_path)
            except Exception as e:
                print(f"Error loading {md_dataset_filename}: {e}")
    db.close()

if __name__ == "__main__":
    main()