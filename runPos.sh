java -mx300m -cp './stanford-postagger-2014-01-04/stanford-postagger.jar:' edu.stanford.nlp.tagger.maxent.MaxentTagger -model ./stanford-postagger-2014-01-04/models/english-left3words-distsim.tagger -textFile $1 -tokenize false -outputFormat tsv > pos_output.txt

