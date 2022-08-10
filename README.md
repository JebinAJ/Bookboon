Task 1 (nginx-deploy.yaml)
Volume is added to the nginx-deploy.yaml file using hostPath which have permanent /etc/nginx/conf.d/ directory

Task 2 (cerebro-test.yaml)
Changes made:
- Memory limits given as 2Gi but requested for 20000Gi, so changed the memory request to 1Gi.
- Removed duplicate resources type.
- Changed the image from lmenezes/cerebro:0.9,4 to lmenezes/cerebro:0.9.4
- Given the value of replica as 1
- Changed the initialDelaySeconds of readinessProbe.
- Removed args.

Tested and the pod starts running in couple of minutes.

Task 3 (cerebro-svc.yaml)
A new service file is created which interact with deployment file. Tested using minikube and successfully accessed ato Cerebro GUI 

Task 4
A shell script is writen in bookboon.sh which gives logs and the script is called inside the Dockerfile.

Task 5
Python script is provided as per the requirment.

