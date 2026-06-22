class Pipeline:
    def __init__(self,projectname):
        self.project_name = projectname

    def build(self):
        print("Building project...")

    def test(self):
        print("Testing project...")
    def deploy(self):
        print("Deploying project...")

class JenkinsPipeline(Pipeline):
    def  deploy(self):
         print("Deploying Jenkins...")

p1 = Pipeline("DevopsPipeline")
print(p1.project_name)
p1.build()
p1.test()
p1.deploy()

J1 = JenkinsPipeline("DevopsPipeline")
J1.build()
J1.test()
J1.deploy()