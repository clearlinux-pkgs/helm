#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : helm
Version  : 2.13.1
Release  : 5
URL      : https://github.com/helm/helm/archive/v2.13.1/helm-2.13.1.tar.gz
Source0  : https://github.com/helm/helm/archive/v2.13.1/helm-2.13.1.tar.gz
Source1  : http://localhost/cgit/projects/helm-vendor/snapshot/helm-vendor-2.12.3.tar.xz
Summary  : Container Cluster Manager - CNI plugins
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear CC-BY-SA-4.0 GPL-2.0 GPL-3.0 ISC LGPL-3.0 MIT MPL-2.0
Requires: helm-bin = %{version}-%{release}
Requires: helm-license = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : glide
Patch1: 0002-ignore-glide-cmd-on-build.patch
Patch2: 0003-Build-fixes.patch

%description
Binaries required to provision container networking.

%package bin
Summary: bin components for the helm package.
Group: Binaries
Requires: helm-license = %{version}-%{release}

%description bin
bin components for the helm package.


%package license
Summary: license components for the helm package.
Group: Default

%description license
license components for the helm package.


%prep
%setup -q -n helm-2.13.1
cd ..
%setup -q -T -D -n helm-2.13.1 -b 1
mkdir -p ./
cp -r %{_topdir}/BUILD/helm-vendor-2.12.3/* %{_topdir}/BUILD/helm-2.13.1/./
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565134834
export GCC_IGNORE_WERROR=1
export GOPROXY=file:///usr/share/goproxy
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
## make_prepend content
export GOPATH=/go
mkdir -p /go/src/k8s.io
ln -s /builddir/build/BUILD/helm-2.13.1 /go/src/k8s.io/helm
cd /go/src/k8s.io/helm
## make_prepend end
make  %{?_smp_mflags} bootstrap build


%install
export SOURCE_DATE_EPOCH=1565134834
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/helm
cp LICENSE %{buildroot}/usr/share/package-licenses/helm/LICENSE
cp vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_cloud.google.com_go_LICENSE
cp vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_Azure_go-ansiterm_LICENSE
cp vendor/github.com/Azure/go-autorest/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_Azure_go-autorest_LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-decoder/COPYING %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-encoder/COPYING %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/tomlv/COPYING %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
cp vendor/github.com/MakeNowJust/heredoc/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_MakeNowJust_heredoc_LICENSE
cp vendor/github.com/Masterminds/goutils/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_Masterminds_goutils_LICENSE.txt
cp vendor/github.com/Masterminds/semver/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_Masterminds_semver_LICENSE.txt
cp vendor/github.com/Masterminds/sprig/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_Masterminds_sprig_LICENSE.txt
cp vendor/github.com/Masterminds/vcs/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_Masterminds_vcs_LICENSE.txt
cp vendor/github.com/PuerkitoBio/purell/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_PuerkitoBio_purell_LICENSE
cp vendor/github.com/PuerkitoBio/urlesc/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_PuerkitoBio_urlesc_LICENSE
cp vendor/github.com/asaskevich/govalidator/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_asaskevich_govalidator_LICENSE
cp vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_beorn7_perks_LICENSE
cp vendor/github.com/chai2010/gettext-go/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_chai2010_gettext-go_LICENSE
cp vendor/github.com/cpuguy83/go-md2man/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
cp vendor/github.com/cyphar/filepath-securejoin/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_cyphar_filepath-securejoin_LICENSE
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/dgrijalva/jwt-go/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_dgrijalva_jwt-go_LICENSE
cp vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_distribution_LICENSE
cp vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_docker_LICENSE
cp vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_docker_NOTICE
cp vendor/github.com/docker/docker/contrib/syntax/vim/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_docker_contrib_syntax_vim_LICENSE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.BSD %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
cp vendor/github.com/docker/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_spdystream_LICENSE
cp vendor/github.com/docker/spdystream/LICENSE.docs %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_docker_spdystream_LICENSE.docs
cp vendor/github.com/evanphx/json-patch/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_evanphx_json-patch_LICENSE
cp vendor/github.com/exponent-io/jsonpath/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_exponent-io_jsonpath_LICENSE
cp vendor/github.com/fatih/camelcase/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_fatih_camelcase_LICENSE.md
cp vendor/github.com/ghodss/yaml/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_ghodss_yaml_LICENSE
cp vendor/github.com/go-openapi/jsonpointer/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_go-openapi_jsonpointer_LICENSE
cp vendor/github.com/go-openapi/jsonreference/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_go-openapi_jsonreference_LICENSE
cp vendor/github.com/go-openapi/spec/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_go-openapi_spec_LICENSE
cp vendor/github.com/go-openapi/spec/license.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_go-openapi_spec_license.go
cp vendor/github.com/go-openapi/spec/license_test.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_go-openapi_spec_license_test.go
cp vendor/github.com/go-openapi/swag/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_go-openapi_swag_LICENSE
cp vendor/github.com/gobwas/glob/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_gobwas_glob_LICENSE
cp vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_gogo_protobuf_LICENSE
cp vendor/github.com/golang/groupcache/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_golang_groupcache_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/google/btree/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_google_btree_LICENSE
cp vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_google_gofuzz_LICENSE
cp vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_google_uuid_LICENSE
cp vendor/github.com/googleapis/gnostic/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_googleapis_gnostic_LICENSE
cp vendor/github.com/gophercloud/gophercloud/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_gophercloud_gophercloud_LICENSE
cp vendor/github.com/gosuri/uitable/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_gosuri_uitable_LICENSE
cp vendor/github.com/gosuri/uitable/util/wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_gosuri_uitable_util_wordwrap_LICENSE.md
cp vendor/github.com/gregjones/httpcache/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_gregjones_httpcache_LICENSE.txt
cp vendor/github.com/grpc-ecosystem/go-grpc-prometheus/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_grpc-ecosystem_go-grpc-prometheus_LICENSE
cp vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_hashicorp_golang-lru_LICENSE
cp vendor/github.com/huandu/xstrings/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_huandu_xstrings_LICENSE
cp vendor/github.com/imdario/mergo/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_imdario_mergo_LICENSE
cp vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_inconshreveable_mousetrap_LICENSE
cp vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_json-iterator_go_LICENSE
cp vendor/github.com/mailru/easyjson/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_mailru_easyjson_LICENSE
cp vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_matttproud_golang_protobuf_extensions_LICENSE
cp vendor/github.com/mitchellh/go-wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_mitchellh_go-wordwrap_LICENSE.md
cp vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_modern-go_concurrent_LICENSE
cp vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_modern-go_reflect2_LICENSE
cp vendor/github.com/opencontainers/go-digest/LICENSE.code %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_opencontainers_go-digest_LICENSE.code
cp vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_opencontainers_go-digest_LICENSE.docs
cp vendor/github.com/peterbourgon/diskv/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_peterbourgon_diskv_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_pmezard_go-difflib_LICENSE
cp vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_golang_LICENSE
cp vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_golang_NOTICE
cp vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_model_LICENSE
cp vendor/github.com/prometheus/client_model/ruby/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_model_ruby_LICENSE
cp vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_prometheus_common_LICENSE
cp vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_prometheus_procfs_LICENSE
cp vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_russross_blackfriday_LICENSE.txt
cp vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_shurcooL_sanitized_anchor_name_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_LICENSE.txt
cp vendor/github.com/spf13/cobra/cobra/cmd/license_agpl.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_agpl.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_apache_2.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_apache_2.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_bsd_clause_2.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_2.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_bsd_clause_3.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_3.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_gpl_2.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_2.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_gpl_3.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_3.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_lgpl.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_lgpl.go
cp vendor/github.com/spf13/cobra/cobra/cmd/license_mit.go %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_mit.go
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_spf13_pflag_LICENSE
cp vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_stretchr_testify_LICENSE
cp vendor/github.com/technosophos/moniker/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/vendor_github.com_technosophos_moniker_LICENSE.txt
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_golang.org_x_oauth2_LICENSE
cp vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_golang.org_x_sync_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_golang.org_x_text_LICENSE
cp vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_golang.org_x_time_LICENSE
cp vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_google.golang.org_appengine_LICENSE
cp vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_google.golang.org_genproto_LICENSE
cp vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_google.golang.org_grpc_LICENSE
cp vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_gopkg.in_inf.v0_LICENSE
cp vendor/gopkg.in/square/go-jose.v2/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_gopkg.in_square_go-jose.v2_LICENSE
cp vendor/gopkg.in/square/go-jose.v2/json/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_gopkg.in_square_go-jose.v2_json_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/helm/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_api_LICENSE
cp vendor/k8s.io/apiextensions-apiserver/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_apiextensions-apiserver_LICENSE
cp vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_apimachinery_LICENSE
cp vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_apiserver_LICENSE
cp vendor/k8s.io/cli-runtime/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_cli-runtime_LICENSE
cp vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_client-go_LICENSE
cp vendor/k8s.io/klog/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_klog_LICENSE
cp vendor/k8s.io/kube-openapi/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kube-openapi_LICENSE
cp vendor/k8s.io/kubernetes/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_LICENSE
cp vendor/k8s.io/kubernetes/cluster/juju/layers/kubeapi-load-balancer/copyright %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_cluster_juju_layers_kubeapi-load-balancer_copyright
cp vendor/k8s.io/kubernetes/cluster/juju/layers/kubernetes-master/copyright %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_cluster_juju_layers_kubernetes-master_copyright
cp vendor/k8s.io/kubernetes/cluster/juju/layers/kubernetes-worker/copyright %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_cluster_juju_layers_kubernetes-worker_copyright
cp vendor/k8s.io/kubernetes/logo/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_logo_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_api_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/apiextensions-apiserver/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_apiextensions-apiserver_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_apimachinery_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_apiserver_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/cli-runtime/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_cli-runtime_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_client-go_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/cloud-provider/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_cloud-provider_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/cluster-bootstrap/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_cluster-bootstrap_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/code-generator/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_code-generator_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/csi-api/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_csi-api_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/kube-aggregator/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-aggregator_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/kube-controller-manager/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-controller-manager_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/kube-proxy/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-proxy_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/kube-scheduler/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-scheduler_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/kubelet/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kubelet_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/metrics/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_metrics_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/sample-apiserver/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_sample-apiserver_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/sample-cli-plugin/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_sample-cli-plugin_LICENSE
cp vendor/k8s.io/kubernetes/staging/src/k8s.io/sample-controller/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_sample-controller_LICENSE
cp vendor/k8s.io/kubernetes/third_party/forked/godep/License %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_godep_License
cp vendor/k8s.io/kubernetes/third_party/forked/golang/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_golang_LICENSE
cp vendor/k8s.io/kubernetes/third_party/forked/gonum/graph/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_gonum_graph_LICENSE
cp vendor/k8s.io/kubernetes/third_party/forked/shell2junit/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_shell2junit_LICENSE
cp vendor/k8s.io/kubernetes/third_party/go-srcimporter/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_go-srcimporter_LICENSE
cp vendor/k8s.io/kubernetes/third_party/intemp/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_intemp_LICENSE
cp vendor/k8s.io/kubernetes/third_party/multiarch/qemu-user-static/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_multiarch_qemu-user-static_LICENSE
cp vendor/k8s.io/kubernetes/third_party/swagger-ui/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_swagger-ui_LICENSE
cp vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_k8s.io_utils_LICENSE
cp vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_sigs.k8s.io_yaml_LICENSE
cp vendor/vbom.ml/util/LICENSE %{buildroot}/usr/share/package-licenses/helm/vendor_vbom.ml_util_LICENSE
true
## install_append content
install -d %{buildroot}/usr/bin
install -D -p -m 0755 bin/{helm,tiller,protoc-gen-go} %{buildroot}/usr/bin/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/helm
/usr/bin/protoc-gen-go
/usr/bin/tiller

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/helm/LICENSE
/usr/share/package-licenses/helm/vendor_cloud.google.com_go_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_Azure_go-ansiterm_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_Azure_go-autorest_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
/usr/share/package-licenses/helm/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
/usr/share/package-licenses/helm/vendor_github.com_MakeNowJust_heredoc_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_Masterminds_goutils_LICENSE.txt
/usr/share/package-licenses/helm/vendor_github.com_Masterminds_semver_LICENSE.txt
/usr/share/package-licenses/helm/vendor_github.com_Masterminds_sprig_LICENSE.txt
/usr/share/package-licenses/helm/vendor_github.com_Masterminds_vcs_LICENSE.txt
/usr/share/package-licenses/helm/vendor_github.com_PuerkitoBio_purell_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_PuerkitoBio_urlesc_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_asaskevich_govalidator_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_beorn7_perks_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_chai2010_gettext-go_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
/usr/share/package-licenses/helm/vendor_github.com_cyphar_filepath-securejoin_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_dgrijalva_jwt-go_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_docker_distribution_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_docker_docker_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_docker_docker_NOTICE
/usr/share/package-licenses/helm/vendor_github.com_docker_docker_contrib_syntax_vim_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
/usr/share/package-licenses/helm/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
/usr/share/package-licenses/helm/vendor_github.com_docker_spdystream_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_docker_spdystream_LICENSE.docs
/usr/share/package-licenses/helm/vendor_github.com_evanphx_json-patch_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_exponent-io_jsonpath_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_fatih_camelcase_LICENSE.md
/usr/share/package-licenses/helm/vendor_github.com_ghodss_yaml_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_go-openapi_jsonpointer_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_go-openapi_jsonreference_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_go-openapi_spec_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_go-openapi_spec_license.go
/usr/share/package-licenses/helm/vendor_github.com_go-openapi_spec_license_test.go
/usr/share/package-licenses/helm/vendor_github.com_go-openapi_swag_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_gobwas_glob_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_gogo_protobuf_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_golang_groupcache_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_google_btree_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_google_gofuzz_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_google_uuid_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_googleapis_gnostic_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_gophercloud_gophercloud_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_gosuri_uitable_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_gosuri_uitable_util_wordwrap_LICENSE.md
/usr/share/package-licenses/helm/vendor_github.com_gregjones_httpcache_LICENSE.txt
/usr/share/package-licenses/helm/vendor_github.com_grpc-ecosystem_go-grpc-prometheus_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_hashicorp_golang-lru_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_huandu_xstrings_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_imdario_mergo_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_json-iterator_go_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_mailru_easyjson_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_matttproud_golang_protobuf_extensions_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_mitchellh_go-wordwrap_LICENSE.md
/usr/share/package-licenses/helm/vendor_github.com_modern-go_concurrent_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_modern-go_reflect2_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_opencontainers_go-digest_LICENSE.code
/usr/share/package-licenses/helm/vendor_github.com_opencontainers_go-digest_LICENSE.docs
/usr/share/package-licenses/helm/vendor_github.com_peterbourgon_diskv_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_golang_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_golang_NOTICE
/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_model_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_prometheus_client_model_ruby_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_prometheus_common_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_prometheus_procfs_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_russross_blackfriday_LICENSE.txt
/usr/share/package-licenses/helm/vendor_github.com_shurcooL_sanitized_anchor_name_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_agpl.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_apache_2.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_2.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_bsd_clause_3.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_2.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_gpl_3.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_lgpl.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_cobra_cobra_cmd_license_mit.go
/usr/share/package-licenses/helm/vendor_github.com_spf13_pflag_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_stretchr_testify_LICENSE
/usr/share/package-licenses/helm/vendor_github.com_technosophos_moniker_LICENSE.txt
/usr/share/package-licenses/helm/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/helm/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/helm/vendor_golang.org_x_oauth2_LICENSE
/usr/share/package-licenses/helm/vendor_golang.org_x_sync_LICENSE
/usr/share/package-licenses/helm/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/helm/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/helm/vendor_golang.org_x_time_LICENSE
/usr/share/package-licenses/helm/vendor_google.golang.org_appengine_LICENSE
/usr/share/package-licenses/helm/vendor_google.golang.org_genproto_LICENSE
/usr/share/package-licenses/helm/vendor_google.golang.org_grpc_LICENSE
/usr/share/package-licenses/helm/vendor_gopkg.in_inf.v0_LICENSE
/usr/share/package-licenses/helm/vendor_gopkg.in_square_go-jose.v2_LICENSE
/usr/share/package-licenses/helm/vendor_gopkg.in_square_go-jose.v2_json_LICENSE
/usr/share/package-licenses/helm/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/helm/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/helm/vendor_k8s.io_api_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_apiextensions-apiserver_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_apimachinery_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_apiserver_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_cli-runtime_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_client-go_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_klog_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kube-openapi_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_cluster_juju_layers_kubeapi-load-balancer_copyright
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_cluster_juju_layers_kubernetes-master_copyright
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_cluster_juju_layers_kubernetes-worker_copyright
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_logo_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_api_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_apiextensions-apiserver_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_apimachinery_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_apiserver_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_cli-runtime_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_client-go_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_cloud-provider_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_cluster-bootstrap_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_code-generator_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_csi-api_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-aggregator_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-controller-manager_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-proxy_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kube-scheduler_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_kubelet_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_metrics_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_sample-apiserver_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_sample-cli-plugin_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_staging_src_k8s.io_sample-controller_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_godep_License
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_golang_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_gonum_graph_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_forked_shell2junit_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_go-srcimporter_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_intemp_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_multiarch_qemu-user-static_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_kubernetes_third_party_swagger-ui_LICENSE
/usr/share/package-licenses/helm/vendor_k8s.io_utils_LICENSE
/usr/share/package-licenses/helm/vendor_sigs.k8s.io_yaml_LICENSE
/usr/share/package-licenses/helm/vendor_vbom.ml_util_LICENSE
