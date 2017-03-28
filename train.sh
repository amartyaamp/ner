#preprocess pos
if [ $# -eq 0 ]; then
	echo "No arguments provided. Usage - ./train.sh <train-file-name>"
        exit 1
fi

./runPos.sh $1
echo "[pos_output.txt generated]"

#preprocess to create the input to be fed to the crf 
python RemStopWord.py $1 train
echo "[created input_int generated ]"
java -cp $MALLET_INC cc.mallet.fst.SimpleTagger --train true --test lab  --training-proportion 0.6 --threads 2 --iterations 1000 --model-file a3crf int_input.txt

echo "[training done]"

