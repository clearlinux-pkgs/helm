PKG_NAME := helm
URL = https://github.com/helm/helm/archive/v3.9.2/helm-3.9.2.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/helm-vendor/snapshot/helm-vendor-3.9.2.tar.xz ./

include ../common/Makefile.common
