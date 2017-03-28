if [ $# -eq 0 ]; then
	echo "No arguments provided. Usage - ./run.sh <inputfilename> <outputfilename>"
        exit 1
fi

./runPos.sh $1
echo "[pos_output.txt generated]"

#preprocess to create the input to be fed to the crf 
python RemStopWord.py $1 test 
echo "[created int_input  ]"

#run acrf to get labels
java -cp $MALLET_INC cc.mallet.fst.SimpleTagger --model-file a3crf int_input.txt > output.txt

echo "[created output.txt]"
#create the final output
python createOutput.py inputfile.txt output.txt $2
echo "[output generated]"
