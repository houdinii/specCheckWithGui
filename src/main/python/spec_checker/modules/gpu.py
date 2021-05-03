import GPUtil


class GpuRecord:
    """
    Single record of GPU item
    """
    def __init__(self, gpu_id=0, gpu_name=None, gpu_load=None, gpu_free_memory=None,
                 gpu_used_memory=None, gpu_total_memory=None, gpu_temperature=None):
        self.gpu_id = gpu_id
        self.gpu_name = gpu_name
        self.gpu_load = gpu_load
        self.gpu_free_memory = gpu_free_memory
        self.gpu_used_memory = gpu_used_memory
        self.gpu_total_memory = gpu_total_memory
        self.gpu_temperature = gpu_temperature

    def __repr__(self):
        return f"<GpuRecord gpu_name:{self.gpu_name} gpu_load:{self.gpu_load}>"

    def __str__(self):
        return f"""
GPU Information:
GPU ID: {self.gpu_id}
GPU Name: {self.gpu_name}
GPU Load: {self.gpu_load}
GPU Free Memory: {self.gpu_free_memory}
GPU Used Memory: {self.gpu_used_memory}
GPU Total Memory: {self.gpu_total_memory}
GPU Temperature: {self.gpu_temperature}"""


class GpuRecords:
    """
    A list of GPU Records
    """
    def __init__(self, gpu_record_list=None):
        # Check if all list items are GpuRecord and if so, add them to self.
        if gpu_record_list and all(isinstance(x, GpuRecord) for x in gpu_record_list):
            self.list = gpu_record_list
        else:
            self.list = []

    def addRecord(self, gpu_record):
        if isinstance(gpu_record, GpuRecord):
            self.list.append(gpu_record)

    def test(self):
        gpus = GPUtil.getGPUs()
        self.gpu_record_list = []
        for gpu in gpus:
            gpu_record = GpuRecord(
                gpu_id=gpu.id,
                gpu_name=f"{gpu.name}",
                gpu_load=f"{gpu.load * 100}%",
                gpu_free_memory=f"{gpu.memoryFree}MB",
                gpu_used_memory=f"{gpu.memoryUsed}MB",
                gpu_total_memory=f"{gpu.memoryTotal}MB",
                gpu_temperature=f"{gpu.temperature} °C")

            self.list.append(gpu_record)
        return self

    def __repr__(self):
        return f"<GpuRecords total_records:{len(self.list)}>"

    def __str__(self):
        if len(self.list) > 0:
            return f"""
First GPU Record:
GPU ID: {self.list[0].gpu_id}
GPU Name: {self.list[0].gpu_name}
GPU Load: {self.list[0].gpu_load}
GPU Free Memory: {self.list[0].gpu_free_memory}
GPU Used Memory: {self.list[0].gpu_used_memory}
GPU Total Memory: {self.list[0].gpu_total_memory}
GPU Temperature: {self.list[0].gpu_temperature}"""
        else:
            return "No GPUs Found!"

