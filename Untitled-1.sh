# bash command to download the tar.gz file 
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$1LePo57dJcgzoK4uiI_48S01Etck7w_5f" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=1LePo57dJcgzoK4uiI_48S01Etck7w_5f" -o supplier-data.tar.gz && sudo rm -rf cookie

# bash command to download the tar.gz file using bash script
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz