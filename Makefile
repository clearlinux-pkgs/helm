PKG_NAME := helm
URL = https://github.com/helm/helm/archive/v2.14.3/helm-2.14.3.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/helm-vendor/snapshot/helm-vendor-2.14.3.tar.xz ./

include ../common/Makefile.common
