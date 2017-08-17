#!/bin/bash
set +x

if [ $# -ne 2 ];then
	echo "magic.sh source_file/dir target_dir"
	exit -1
fi

bashpath=`dirname $0`
echo "basepath: $bashpath"

srcford=$1
tgd=$2

ips=()
macs=()
users=()
i=0
log=".superscp.log"
touch $log

datafname="${bashpath}/.data.superscp"
if [ ! -f $datafname ];then
	echo "can not find data file" >> $log 2>&1
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
	if [ ! -d ~/xxxxtmp ];then
		echo "superscp failed" >> $log 2>&1
		exit -1
	fi
	mv ~/xxxxtmp/$srcford $tgd
	rm ~/xxxxtmp -rf
	exit 0
fi
user=${users[$idx]}
echo "----$ip---$idx----$user------"

if [ $idx -eq 1 ];then
	echo "this is source host"
	if [ -d ~/xxxxtmp ];then
		rm -rf ~/xxxxtmp
	fi
	mkdir ~/xxxxtmp
	if [ ! -e ${srcford} ];then
		echo "----invalid source file or dir parameter----"
		exit -1
	fi
	if [ -d $srcford ];then
		cp -r $srcford ~/xxxxtmp/
		cd $srcford
		srcford=`pwd`
		cd -
	elif [ -f $srcford ];then
		cp $srcford ~/xxxxtmp/
	fi
	cp ${bashpath}/magic.sh ~/xxxxtmp/
	cp ${datafname} ~/xxxxtmp/
	srcford=$(basename $srcford)
	echo "-----new name=${srcford}--------"
fi

scp -r ~/xxxxtmp ${user}@${ip}:~/
echo "scp return: $?"
set -x
ssh ${user}@${ip} "~/xxxxtmp/magic.sh $srcford /tmp"
echo "ssh return: $?"
rm ~/xxxxtmp -rf

