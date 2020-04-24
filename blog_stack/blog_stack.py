from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.onprem.network import Nginx
from diagrams.onprem.container import Docker


with Diagram("Blog stack", show=False):
    with Cluster("AWS"):
        dns = Route53("meu.blog.br")

        with Cluster("us-east-1"):
            blog_vpc = VPC("blog_vpc")

            dns >> blog_vpc

            with Cluster("blog_vpc"):
                nginx = Nginx("proxy")
                docker = Docker("blog")
                postgres = RDS("postgres")

                blog_vpc >> nginx >> docker >> postgres
