import ray


@ray.remote(num_cpus=0)
class TemporalReporterActor:
    def __init__(self) -> None:
        pass
