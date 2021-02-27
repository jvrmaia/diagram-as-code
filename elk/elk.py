from diagrams import Cluster, Diagram
from diagrams.onprem.database import Cassandra
from diagrams.onprem.monitoring import Kibana
from diagrams.onprem.search import Elasticsearch
from diagrams.onprem.logging import Logstash


with Diagram("ELK", show=False):
    with Cluster("cassandra"):
        cassandra_cluster = [Cassandra("c01"),
                             Cassandra("c02"),
                             Cassandra("c03"),
                             Cassandra("c04"),
                             Cassandra("c05")]

    logstash = Logstash("logstash")
    elasticsearch = Elasticsearch("elasticsearch")
    kibana = Kibana("kibana")

    cassandra_cluster >> logstash >> elasticsearch >> kibana
