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