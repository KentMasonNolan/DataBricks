from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.remote(
    host="https://<workspace-instance-name>",
    token="<access-token-value>",
    cluster_id="<cluster-id>"
).getOrCreate()

# Or...
from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.remote(
    "sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>"
).getOrCreate()
