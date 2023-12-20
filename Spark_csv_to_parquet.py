import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["Spark_csv_to_parquet"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1703082236733 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={
        "paths": ["s3://dcsc-raw-data/youtube/raw_statistics/"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1703082236733",
)

# Script generated for node Amazon S3
AmazonS3_node1703082333771 = glueContext.getSink(
    path="s3://dcsc-cleaned-data/youtube/raw_statistics/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["category_id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1703082333771",
)
AmazonS3_node1703082333771.setCatalogInfo(
    catalogDatabase="dcsc-cleaned-database", catalogTableName="Cleaned_Datacatalog"
)
AmazonS3_node1703082333771.setFormat("glueparquet")
AmazonS3_node1703082333771.writeFrame(AmazonS3_node1703082236733)
job.commit()