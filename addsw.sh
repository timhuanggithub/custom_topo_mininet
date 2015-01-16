if [ $1 = "1" ];then
	sudo ovs-vsctl set-controller s1 tcp:10.211.55.2:6633
elif [ $1 = "345" ]; then
	sudo ovs-vsctl set-controller s3 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s4 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s5 tcp:10.211.55.2:6633
elif [ $1 = "345910" ]; then
	sudo ovs-vsctl set-controller s3 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s4 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s5 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s9 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s10 tcp:10.211.55.2:6633
elif [ $1 = "34591013" ]; then
	sudo ovs-vsctl set-controller s3 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s4 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s5 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s9 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s10 tcp:10.211.55.2:6633
	sudo ovs-vsctl set-controller s13 tcp:10.211.55.2:6633
fi
