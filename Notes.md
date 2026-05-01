set GOOGLE_APPLICATION_CREDENTIALS=/mnt/c/Users/think/Desktop/MLOps Bootcamp/Anime_Recomendation_Project/learningprojects-486111-a374659bd25c.json 
=> for activation the google cli 
export GOOGLE_APPLICATION_CREDENTIALS="/mnt/c/Users/think/Desktop/MLOps Bootcamp/Anime_Recomendation_Project/learningprojects-486111-a374659bd25c.json"


when we working with dvc 
+ the artifact folder (hasn't exist in the github , else it'll through an exception )
 
+ then run dvc init => then run this commend dvc artifacts/raw .....(in this case is the file whose contain all the files for code sources ) (all files you need them )

+ push to github 
 
+  add `dvc-gs` to the requirement txt as an package

+ `dvc add -d myremote gs://anime_recomendation-dvc-bucket/`
- myremote :represent the dvc_name
 `-d`: parameters means makes the remote default  
- add the artifact files into to with commend => `dvc add artifacts/model artifacts/model_checkpoint artifacts/raw artifacts/weights artifacts/processed`


## the right code for the installation the Kubernetes & Google cli is (in the CI CD deployment)

''' 
+ Enter container:

docker exec -u root -it jenkins-dind-2 bash

+ Clean previous wrong config (IMPORTANT):

`rm -f /etc/apt/sources.list.d/google-cloud-sdk.list`

`rm -f /etc/apt/keyrings/google-cloud.gpg`

+ Install required packages:

`apt-get update`
`apt-get install -y curl ca-certificates gnupg`

+ Add Google Cloud key (correct way):

`mkdir -p /etc/apt/keyrings`
`curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
  | gpg --dearmor -o /etc/apt/keyrings/google-cloud.gpg`

+ Add repository (IMPORTANT: correct syntax):

`echo "deb [signed-by=/etc/apt/keyrings/google-cloud.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
  | tee /etc/apt/sources.list.d/google-cloud-sdk.list`

+ Update again (THIS STEP MUST WORK)

`apt-get update
`
+ Install packages:

`apt-get install -y google-cloud-sdk kubectl`

`google-cloud-sdk-gke-gcloud-auth-plugin`
'''
> then we make a check if the nessecary librarie is installed :
+ `kubectl version --client`
+ `gcloud --version`