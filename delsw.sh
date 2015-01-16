if [ $1 = "1" ];then
	sudo ovs-vsctl set-fail-mode s1 standalone
	sudo ovs-vsctl del-controller s1
elif [ $1 = "345" ]; then
	sudo ovs-vsctl set-fail-mode s3 standalone
	sudo ovs-vsctl set-fail-mode s4 standalone
	sudo ovs-vsctl set-fail-mode s5 standalone
	sudo ovs-vsctl del-controller s3
	sudo ovs-vsctl del-controller s4
	sudo ovs-vsctl del-controller s5
elif [ $1 = "345910" ]; then
	sudo ovs-vsctl set-fail-mode s3 standalone
	sudo ovs-vsctl set-fail-mode s4 standalone
	sudo ovs-vsctl set-fail-mode s5 standalone
	sudo ovs-vsctl set-fail-mode s5 standalone
	sudo ovs-vsctl set-fail-mode s9 standalone
	sudo ovs-vsctl set-fail-mode s10 standalone
	sudo ovs-vsctl del-controller s3
	sudo ovs-vsctl del-controller s4
	sudo ovs-vsctl del-controller s5
	sudo ovs-vsctl del-controller s9
	sudo ovs-vsctl del-controller s10
elif [ $1 = "34591013" ]; then
	sudo ovs-vsctl set-fail-mode s3 standalone
	sudo ovs-vsctl set-fail-mode s4 standalone
	sudo ovs-vsctl set-fail-mode s5 standalone
	sudo ovs-vsctl set-fail-mode s5 standalone
	sudo ovs-vsctl set-fail-mode s9 standalone
	sudo ovs-vsctl set-fail-mode s10 standalone
	sudo ovs-vsctl set-fail-mode s13 standalone
	sudo ovs-vsctl del-controller s3
	sudo ovs-vsctl del-controller s4
	sudo ovs-vsctl del-controller s5
	sudo ovs-vsctl del-controller s9
	sudo ovs-vsctl del-controller s10
	sudo ovs-vsctl del-controller s13
fi
