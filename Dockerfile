FROM centos:7

RUN yum check-update || true
RUN yum upgrade -y

# To install usefull tools
RUN yum install -y \
	tree

# To update EPEL repo to install python development environment libraries.
RUN yum --enablerepo=extras install epel-release -y

# To install python development environment library
RUN yum install -y \
	python-dev \
	python-pip


#To install scrapy and depedency 
# https://clasense4.wordpress.com/2015/11/25/how-to-install-scrapy-on-centos-7/
RUN yum install python-pip -y \
	python-devel \
	gcc \
	gcc-devel \
	libxml2 \
	libxml2-devel \
	libxslt \
	libxslt-devel \
	openssl \
	openssl-devel \
	libffi \
	libffi-devel	


RUN pip install --upgrade pip

RUN pip install scrapy
