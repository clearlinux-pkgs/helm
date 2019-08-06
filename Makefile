PKG_NAME := helm
URL = https://github.com/helm/helm/archive/v2.13.1/helm-2.13.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/helm-vendor/snapshot/helm-vendor-2.12.3.tar.xz ./

include ../common/Makefile.common
