eg10() {
    local data="data/jedit-4.1.arff"               # edit this line to change the data
    local learners="j48 jrip nb rbfnet bnet zeroR" # edit this line to change the leaners
    local goal=true                                # edit this line to hunt for another goal
    
    local i="$Tmp/eg11"
    if [ -f "$i.pd" ]; then
       report pd "$i"
       report pf "$i"
    else
        crossval 5 5 "$data" $Seed $learners | grep $goal >"$i"
        gawk  '{print $2,$10}' "$i" > "$i.pd"
        gawk  '{print $2,$11}' "$i" > "$i.pf"
        eg10
   fi
}
