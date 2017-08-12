#!/bin/bash
set +x

if [ $# -ne 3 ];then
	echo "magic.sh source_file/dir target_ip target_dir"
	exit -1
fi

srcford=$1
tgip=$2
tgd=$3

ips=()
macs=()
users=()
i=0

datafname=".data.superscp"
if [ ! -f $datafname ];then
	echo "can not find data file"
	exit -1
fi

while read line
do
	if [ $i -eq 0 ];then
		ips=(${line//,/ })
	elif [ $i -eq 1 ];then
		macs=(${line//,/ })
	elif [ $i -eq 2 ];then
		users=(${line//,/ })
	fi
	((i=i+1))
done < $datafname 

function next_ip() {
	j=0
	while [ $j -lt ${#ips[@]} ] 
	do
		rt=`ifconfig | grep "${macs[$j]}" | wc -l`
		((j=j+1))
		if [ $rt -eq 0 ];then
			continue
		fi
		if [ $j -eq ${#ips[*]} ];then
			echo "end"
			return 255
		fi
		echo "${ips[$j]}"
		return $j 
	done
	echo "no"
	return 255 
}

ip=`next_ip`
idx=$?
if [ "${ip}" == "end" ];then
	echo "finish"
fi
user=${users[$idx]}
echo "----$ip---$idx----$user-"

if [ $idx -eq 1 ];then
	echo "this is source host"
	if [ -d xxxxtmp ];then
		rm -rf xxxxtmp
	fi
	mkdir xxxxtmp
	if [ -d $srcford ];then
		cp -r $srcford xxxxtmp/
	elif [ -f $srcford ];then
		cp $srcford xxxxtmp/
	fi
	cp magic.sh xxxxtmp/
	cp .data.superscp xxxxtmp/
fi

scp -r xxxxtmp ${user}@${ip}:~/
ssh ${user}@${ip} "~/xxxxtmp/magic.sh magic.sh 192.168.122.179 /tmp"

echo "ssh return: $?"

