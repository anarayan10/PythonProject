class AWSResource:
    def __init__(self, resource_name, region):
        self.resource_name = resource_name
        self.region = region

    def display_details(self):
        print("Resource Name:", self.resource_name)
        print("Region:", self.region)


class LambdaFunction(AWSResource):
    def __init__(self, resource_name, region, runtime):
        super().__init__(resource_name, region)
        self.runtime = runtime

    def display_details(self):
        super().display_details()
        print("Runtime:", self.runtime)


l1 = LambdaFunction("my_lambda", "ap-south-1", "python3.12")
l1.display_details()