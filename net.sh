file="3nodes.py"
topo="3nodes"
if [ $1 = "4n1" ];then
	file="4nodes1n.py"
	topo="4nodes1n"
elif [ $1 = "4d" ]; then
	file="4nodes.py"
	topo="4nodes"
elif [ $1 = "9n345" ]; then
	file="9nodes345n.py"
	topo="9nodes345n"
elif [ $1 = "11n345910" ]; then
    file="11nodes345910n.py"
    topo="11nodes345910n"
elif [ $1 = "13n34591013" ]; then
    file="13nodes34591013n.py"
    topo="13nodes34591013n"
fi

sudo mn --custom ~/mininet/custom/$file --mac --topo $topo --controller remote,ip=10.211.55.2,port=6633
