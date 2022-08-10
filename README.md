Task 1 (nginx-deploy.yaml)
Volume is added to the nginx-deploy.yaml file using hostPath which have permanent /etc/nginx/conf.d/ directory

Task 2 (deployment-test.yaml)
Fix problems occurring in this file. In the result we want to have a running pod.

Task 3 (deployment-svc.yaml)
After fixing this yaml deployment, create an svc file working with this deployment. It needs to give access to Cerebro GUI after running a "kubectl port-forward svc" command.

Task 4
A shell script is writen in bookboon.sh which gives logs as Bookboon test and it is called inside Dockerfile.

Task 5
Script is written in python with the requirment provided in the name pythonscript.py

