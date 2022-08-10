Task 1 (nginx-deploy.yaml)
Volume is added to the nginx-deploy.yaml file using hostPath which have permanent /etc/nginx/conf.d/ directory

Task 2 (deployment-test.yaml)
Changes made:
- Memory limits given as 2Gi but requested for 20000Gi, so changed the memory request to 1Gi.
- Removed duplicate resources type.
- Changed the image from lmenezes/cerebro:0.9,4 to lmenezes/cerebro:0.9.4
- Given the value of replica as 1
- Changed the initialDelaySeconds of readinessProbe.
- Removed args.

Task 3 (deployment-svc.yaml)
After fixing this yaml deployment, create an svc file working with this deployment. It needs to give access to Cerebro GUI after running a "kubectl port-forward svc" command.

Task 4
A shell script is writen in bookboon.sh which gives logs as Bookboon test and it is called inside Dockerfile.

Task 5
Script is written in python with the requirment provided in the name pythonscript.py

