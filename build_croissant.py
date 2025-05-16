import mlcroissant as mlc

# FileObjects and FileSets define the resources of the dataset.
distribution = [
    mlc.FileObject(
        id="github-repository",
        name="github-repository",
        description="MonopathPatientDAGs repository on GitHub.",
        content_url="https://github.com/shloknatarajan/MonopathPatientDAGsDataset",
        encoding_formats=["git+https"],
        sha256="main",
    ),
    mlc.FileSet(
        id="jsonl-files",
        name="jsonl-files",
        description="JSONL files are hosted on the GitHub repository.",
        contained_in=["github-repository"],
        encoding_formats=["application/jsonlines"],
        includes="dataset/dynamic_data.jsonl",
    ),
]
record_sets = [
    # RecordSets contains records in the dataset.
    mlc.RecordSet(
        id="jsonl",
        name="jsonl",
        # Each record has one or many fields...
        fields=[
            # Fields can be extracted from the FileObjects/FileSets.
            mlc.Field(
                id="jsonl/graph_id",
                name="graph_id",
                description="",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    # Extract the field from the column of a FileObject/FileSet:
                    extract=mlc.Extract(column="graph_id"),
                ),
            ),
            mlc.Field(
                id="jsonl/is_control",
                name="is_control",
                description="Whether the graph is a control graph.",
                data_types=mlc.DataType.BOOL,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="is_control"),
                ),
            ),
            mlc.Field(
                id="jsonl/synthetic_output",
                name="synthetic_output",
                description="The synthetic output history.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="synthetic_output"),
                ),
            ),
            mlc.Field(
                id="jsonl/model",
                name="model",
                description="The model used to generate the synthetic output.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="model"),
                ),
            ),
            mlc.Field(
                id="jsonl/node_path_used",
                name="node_path_used",
                description="Node path in string format (needs to be parsed to array)",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="node_path_used"),
                ),
            ),
            mlc.Field(
                id="jsonl/node_path_true",
                name="node_path_true",
                description="The longest path of the directed acyclic graph",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="node_path_used"),
                ),
            ),
            mlc.Field(
                id="jsonl/uid",
                name="uid",
                description="uid",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="uid"),
                ),
            ),
            mlc.Field(
                id="jsonl/graph_json",
                name="graph_json",
                description="JSON containing the history node/edges. Stored as a string but can be parsed",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="graph_json"),
                ),
            ),
        ],
    )
]

# Metadata contains information about the dataset.
metadata = mlc.Metadata(
    name="MonopathPatientDAGs",
    # Descriptions can contain plain text or markdown.
    description=(
        "We present a modular framework that transforms free-text case reports " 
        "into Monopath directed acyclic graphs (DAGs) that represent temporally ordered"
        "and semantically grounded patient trajectories. DAGs are a natural fit for model-ing"
        "clinical narratives as they encode time-ordered clinical states and transitions,"
        "supporting branching and causal reasoning. These graphs serve as generative tem-plates"
        "for clinically grounded synthetic data and support downstream tasks such as"
        "patient similarity retrieval and trajectory-aware data augmentation."
    ),
    cite_as=(
       ""
    ),
    url="https://github.com/DaneshjouLab/DynamicData/",
    distribution=distribution,
    record_sets=record_sets,
)

## Save the metadata as the croissant.json file
import json

with open("croissant.json", "w") as f:
  content = metadata.to_json()
  content = json.dumps(content, indent=2)
  print(content)
  f.write(content)
  f.write("\n")  # Terminate file with newline
     