from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


with Diagram("Grouped Workers", show=True, direction="TB"):
    (
        ELB("Load Balancer")
        >> [
            EC2("Worker1"),
            EC2("Worker2"),
            EC2("Worker3"),
            EC2("Worker4"),
            EC2("Worker5"),
        ]
        >> RDS("Events")
    )
