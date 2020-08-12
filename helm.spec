#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : helm
Version  : 3.3.0
Release  : 23
URL      : https://github.com/helm/helm/archive/v3.3.0/helm-3.3.0.tar.gz
Source0  : https://github.com/helm/helm/archive/v3.3.0/helm-3.3.0.tar.gz
Source1  : http://localhost/cgit/projects/helm-vendor/snapshot/helm-vendor-3.3.0.tar.xz
Summary  : The Kubernetes Package Manager
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC MIT MPL-2.0 Zlib
Requires: helm-bin = %{version}-%{release}
Requires: helm-license = %{version}-%{release}
BuildRequires : buildreq-golang

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of
pre-configured Kubernetes resources.

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
%setup -q -n helm-3.3.0
cd %{_builddir}
tar xf %{_sourcedir}/helm-vendor-3.3.0.tar.xz
cd %{_builddir}/helm-3.3.0
mkdir -p ./
cp -r %{_builddir}/helm-vendor-3.3.0/* %{_builddir}/helm-3.3.0/./

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597257292
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  -f Makefile build VERSION=v%{version} GOFLAGS='-mod=vendor -buildmode=pie -v'


%install
export SOURCE_DATE_EPOCH=1597257292
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/helm
cp %{_builddir}/helm-3.3.0/LICENSE %{buildroot}/usr/share/package-licenses/helm/e625f9555286c04d831ffbaf5b27a8668f1aa1a7
cp %{_builddir}/helm-vendor-3.3.0/vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/helm/836ef1b46953afdb78ce3929bc6831ca83620b65
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Azure/go-autorest/autorest/LICENSE %{buildroot}/usr/share/package-licenses/helm/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Azure/go-autorest/autorest/adal/LICENSE %{buildroot}/usr/share/package-licenses/helm/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Azure/go-autorest/autorest/date/LICENSE %{buildroot}/usr/share/package-licenses/helm/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Azure/go-autorest/logger/LICENSE %{buildroot}/usr/share/package-licenses/helm/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Azure/go-autorest/tracing/LICENSE %{buildroot}/usr/share/package-licenses/helm/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/helm/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/DATA-DOG/go-sqlmock/LICENSE %{buildroot}/usr/share/package-licenses/helm/d67b593949431da7b7972a3517af80b377ad8598
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/MakeNowJust/heredoc/LICENSE %{buildroot}/usr/share/package-licenses/helm/43c02fe811dfc96363cdd8ec756ecc728ab845a9
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Masterminds/goutils/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Masterminds/semver/v3/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/020acfcf6d6bd6d701d19bd16f49d0bf18441779
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Masterminds/sprig/v3/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/535e3badf5b532d842627b504976fbb93bc2d8b8
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Masterminds/squirrel/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/51ed3a4a1e142924d057f46a167c1e725da33ea6
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Masterminds/vcs/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/19faac93bab978326d06e3b96bbf41d495ce2a51
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/helm/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/package-licenses/helm/56b820712432e458f05f883566ca8cd85dcdaad5
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/PuerkitoBio/purell/LICENSE %{buildroot}/usr/share/package-licenses/helm/33cd8e150548e595fbe201c6ca9df582976e71db
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/PuerkitoBio/urlesc/LICENSE %{buildroot}/usr/share/package-licenses/helm/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/Shopify/logrus-bugsnag/LICENSE %{buildroot}/usr/share/package-licenses/helm/91048638b5f60b9649fdaf66d1c921f15ce5f963
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/asaskevich/govalidator/LICENSE %{buildroot}/usr/share/package-licenses/helm/f0524399083fa802c72bc733a5e12ed1342c650f
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/helm/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/bshuster-repo/logrus-logstash-hook/LICENSE %{buildroot}/usr/share/package-licenses/helm/22fb4edb0c69c2548d682c09b6ba589e4f1529af
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/bugsnag/bugsnag-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/27144fa397dd4ece1028c9ddc96063cff4cf9735
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/bugsnag/osext/LICENSE %{buildroot}/usr/share/package-licenses/helm/0650245a32cb5605e02d181a86e03d917887e73e
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/bugsnag/panicwrap/LICENSE %{buildroot}/usr/share/package-licenses/helm/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/7be82c1a81e7197640a88df91dc82d64b77c7acd
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/containerd/cgroups/LICENSE %{buildroot}/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/containerd/containerd/LICENSE %{buildroot}/usr/share/package-licenses/helm/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/cyphar/filepath-securejoin/LICENSE %{buildroot}/usr/share/package-licenses/helm/8fb92f475d78da1315877a719c6856fc64531d30
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/helm/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/deislabs/oras/LICENSE %{buildroot}/usr/share/package-licenses/helm/03e1fe6fd0bc6d73c3cd3370d5f0a73c4fcb60d6
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/dgrijalva/jwt-go/LICENSE %{buildroot}/usr/share/package-licenses/helm/b132e03c6b6bd85fbc2394f808acae8f5d0ebaf0
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/cli/LICENSE %{buildroot}/usr/share/package-licenses/helm/878e7d86573d6c8ff65d2eaab294734b3f4d3d81
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/cli/NOTICE %{buildroot}/usr/share/package-licenses/helm/5476f2f91673ef040f1956907e7f45e72d5e11ee
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/package-licenses/helm/c700a8b9312d24bdc57570f7d6a131cf63d89016
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/docker-credential-helpers/LICENSE %{buildroot}/usr/share/package-licenses/helm/f3eab54cb1736b419ef75b8c44bea2b17614bd31
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/helm/20b06a68cf65738d43afa04acce0126f341c77f8
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/helm/5476f2f91673ef040f1956907e7f45e72d5e11ee
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/go-connections/LICENSE %{buildroot}/usr/share/package-licenses/helm/3110e55750143a84918d7423febc9c83a55bc28c
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/go-metrics/LICENSE.code %{buildroot}/usr/share/package-licenses/helm/376caa2cd54c4196280157d071524614350e7ce8
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/go-metrics/LICENSE.docs %{buildroot}/usr/share/package-licenses/helm/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/helm/3110e55750143a84918d7423febc9c83a55bc28c
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/libtrust/LICENSE %{buildroot}/usr/share/package-licenses/helm/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/helm/c6821d75aac4a65fae7d56a425e304beb3689c26
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/docker/spdystream/LICENSE.docs %{buildroot}/usr/share/package-licenses/helm/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/emicklei/go-restful/LICENSE %{buildroot}/usr/share/package-licenses/helm/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/evanphx/json-patch/LICENSE %{buildroot}/usr/share/package-licenses/helm/773bfa66739275c14ad854cdef4f550973fbaee6
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/exponent-io/jsonpath/LICENSE %{buildroot}/usr/share/package-licenses/helm/9a06b8c36ca519c5a7c67f102bf5d03aae470fa1
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/fatih/color/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/563519fec7769aaec054ee06cb429f39f0fdab89
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/ghodss/yaml/LICENSE %{buildroot}/usr/share/package-licenses/helm/271aeaf56ee621c5accfc2a9db0b10717e038eaf
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/go-openapi/jsonpointer/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/go-openapi/jsonreference/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/go-openapi/spec/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/go-openapi/spec/license.go %{buildroot}/usr/share/package-licenses/helm/555e9ac61d94352b3c2935e77b51fc6dc31d4822
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/go-openapi/swag/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gobwas/glob/LICENSE %{buildroot}/usr/share/package-licenses/helm/1b2d963c77ddfc6454ca369fc4884e87e256a2e1
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gofrs/flock/LICENSE %{buildroot}/usr/share/package-licenses/helm/c9db89ee093e8877dec1561919147d3680182146
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/helm/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/golang/groupcache/LICENSE %{buildroot}/usr/share/package-licenses/helm/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/helm/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/google/btree/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/helm/7080652cc78cd9855d39e324529a3b5f3745dcd6
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/helm/08021ae73f58f423dd6e7b525e81cf2520f7619e
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/googleapis/gnostic/LICENSE %{buildroot}/usr/share/package-licenses/helm/5a7d7df655ba40478fae80a6abafc6afc36f9b6a
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gophercloud/gophercloud/LICENSE %{buildroot}/usr/share/package-licenses/helm/01e537267fca176b08cd25a4e6e6a7092ed3c734
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gorilla/handlers/LICENSE %{buildroot}/usr/share/package-licenses/helm/51bad2bd8dc245d3cd45f69b6dd4e52f97131e6a
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gorilla/mux/LICENSE %{buildroot}/usr/share/package-licenses/helm/8bc609022fad5f9e8aec8889ab9cb195afd5ecc5
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gosuri/uitable/LICENSE %{buildroot}/usr/share/package-licenses/helm/5cc38e91ed50df624def2d682d8e033d25917167
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gosuri/uitable/util/wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/d676a57141ac47c27699fc8b03e1a2e59abb96ef
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/gregjones/httpcache/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/21b9915e693e6d81b3908c83fb59687aec46029b
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/helm/ece3df1263c100f93c427face535a292723d38e7
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/huandu/xstrings/LICENSE %{buildroot}/usr/share/package-licenses/helm/8758b52c623c08eff9cadbd0f0e1541085e9984d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/imdario/mergo/LICENSE %{buildroot}/usr/share/package-licenses/helm/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/helm/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/jmoiron/sqlx/LICENSE %{buildroot}/usr/share/package-licenses/helm/b0eab1611332b5c5d43728e84e6bc47569775bc0
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/helm/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/konsorten/go-windows-terminal-sequences/LICENSE %{buildroot}/usr/share/package-licenses/helm/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/lann/builder/LICENSE %{buildroot}/usr/share/package-licenses/helm/b6744ad41956605ebba2359b9cb728a7a68664d7
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/lann/ps/LICENSE %{buildroot}/usr/share/package-licenses/helm/b010e169e965af2c274a7001b7e32cd77fd4fd85
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/lib/pq/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/736c20a685418b27e6992d88c0959152991d33bf
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/liggitt/tabwriter/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mailru/easyjson/LICENSE %{buildroot}/usr/share/package-licenses/helm/554fb441fbb1607579b7c9f8e9d7fab5d00e3a51
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/helm/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/helm/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/helm/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mattn/go-shellwords/LICENSE %{buildroot}/usr/share/package-licenses/helm/f7f33fde14de785a3ac53f250bb746ba30844639
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/helm/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mitchellh/copystructure/LICENSE %{buildroot}/usr/share/package-licenses/helm/d676a57141ac47c27699fc8b03e1a2e59abb96ef
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mitchellh/go-wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/helm/d676a57141ac47c27699fc8b03e1a2e59abb96ef
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/mitchellh/reflectwalk/LICENSE %{buildroot}/usr/share/package-licenses/helm/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/morikuni/aec/LICENSE %{buildroot}/usr/share/package-licenses/helm/3faf341fbc32621fe1ac089ae2ab7a23980fc189
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/opencontainers/go-digest/LICENSE %{buildroot}/usr/share/package-licenses/helm/93ac97c9679b68518f1fd7de627ce2f77f44082d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/helm/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/opencontainers/image-spec/LICENSE %{buildroot}/usr/share/package-licenses/helm/298850a6cdb155f54cfa44641df70b36228ed031
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/helm/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/peterbourgon/diskv/LICENSE %{buildroot}/usr/share/package-licenses/helm/87a1773b9070fa0f9d4033df28f9bcba336279b1
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/helm/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/helm/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/helm/fd6460234f122a19f21affb6d6885269340b9176
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/rubenv/sql-migrate/LICENSE %{buildroot}/usr/share/package-licenses/helm/45d072ce2a777c39a639bfce7cb3c27132ea3a64
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/rubenv/sql-migrate/sqlparse/LICENSE %{buildroot}/usr/share/package-licenses/helm/40ed8341d216cd2b3ecacc876babb86de444b800
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/helm/c111106ab0af1873aa6350f797759fe1519c8be1
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/helm/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/spf13/cast/LICENSE %{buildroot}/usr/share/package-licenses/helm/feb9285b75d0c82a47d32e7d4dc84eb02db9ee34
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/helm/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/helm/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/helm/892204393ca075d09c8b1c1d880aba1ae0a2b805
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/xeipuuv/gojsonpointer/LICENSE-APACHE-2.0.txt %{buildroot}/usr/share/package-licenses/helm/b7173385030ef97bce57b5b4b78b48763c83aed3
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/xeipuuv/gojsonreference/LICENSE-APACHE-2.0.txt %{buildroot}/usr/share/package-licenses/helm/b7173385030ef97bce57b5b4b78b48763c83aed3
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/xeipuuv/gojsonschema/LICENSE-APACHE-2.0.txt %{buildroot}/usr/share/package-licenses/helm/b7173385030ef97bce57b5b4b78b48763c83aed3
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/yvasiyarov/go-metrics/LICENSE %{buildroot}/usr/share/package-licenses/helm/f4f6a4a62f50348c9f4fa311fd2023d8ed32e380
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/yvasiyarov/gorelic/LICENSE %{buildroot}/usr/share/package-licenses/helm/53b850c91770a865abb0838b1f0eee0476d41f97
cp %{_builddir}/helm-vendor-3.3.0/vendor/github.com/yvasiyarov/newrelic_platform_go/LICENSE %{buildroot}/usr/share/package-licenses/helm/53b850c91770a865abb0838b1f0eee0476d41f97
cp %{_builddir}/helm-vendor-3.3.0/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/helm/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/helm-vendor-3.3.0/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/helm-vendor-3.3.0/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/gopkg.in/gorp.v1/LICENSE %{buildroot}/usr/share/package-licenses/helm/07f029f0501040d2dca397bee81b2ac25a0d1b3b
cp %{_builddir}/helm-vendor-3.3.0/vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/helm/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
cp %{_builddir}/helm-vendor-3.3.0/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/helm/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/helm-vendor-3.3.0/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/helm/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/helm-vendor-3.3.0/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/helm/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/helm-vendor-3.3.0/vendor/gopkg.in/yaml.v3/LICENSE %{buildroot}/usr/share/package-licenses/helm/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
cp %{_builddir}/helm-vendor-3.3.0/vendor/gopkg.in/yaml.v3/NOTICE %{buildroot}/usr/share/package-licenses/helm/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/apiextensions-apiserver/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/cli-runtime/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/component-base/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/klog/LICENSE %{buildroot}/usr/share/package-licenses/helm/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/kube-openapi/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/kubectl/LICENSE %{buildroot}/usr/share/package-licenses/helm/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/helm-vendor-3.3.0/vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/helm-vendor-3.3.0/vendor/sigs.k8s.io/kustomize/LICENSE %{buildroot}/usr/share/package-licenses/helm/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/helm-vendor-3.3.0/vendor/sigs.k8s.io/structured-merge-diff/v3/LICENSE %{buildroot}/usr/share/package-licenses/helm/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/helm-vendor-3.3.0/vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/helm/271aeaf56ee621c5accfc2a9db0b10717e038eaf
true
## install_append content
install -d %{buildroot}/usr/bin
install -D -p -m 0755 bin/helm %{buildroot}/usr/bin/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/helm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/helm/01e537267fca176b08cd25a4e6e6a7092ed3c734
/usr/share/package-licenses/helm/020acfcf6d6bd6d701d19bd16f49d0bf18441779
/usr/share/package-licenses/helm/03e1fe6fd0bc6d73c3cd3370d5f0a73c4fcb60d6
/usr/share/package-licenses/helm/0650245a32cb5605e02d181a86e03d917887e73e
/usr/share/package-licenses/helm/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/helm/07f029f0501040d2dca397bee81b2ac25a0d1b3b
/usr/share/package-licenses/helm/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/helm/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/helm/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/helm/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/helm/19faac93bab978326d06e3b96bbf41d495ce2a51
/usr/share/package-licenses/helm/1b2d963c77ddfc6454ca369fc4884e87e256a2e1
/usr/share/package-licenses/helm/20b06a68cf65738d43afa04acce0126f341c77f8
/usr/share/package-licenses/helm/21b9915e693e6d81b3908c83fb59687aec46029b
/usr/share/package-licenses/helm/22fb4edb0c69c2548d682c09b6ba589e4f1529af
/usr/share/package-licenses/helm/27144fa397dd4ece1028c9ddc96063cff4cf9735
/usr/share/package-licenses/helm/271aeaf56ee621c5accfc2a9db0b10717e038eaf
/usr/share/package-licenses/helm/298850a6cdb155f54cfa44641df70b36228ed031
/usr/share/package-licenses/helm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/helm/308c47a3ea356402d2d14241da9a9f64cf404008
/usr/share/package-licenses/helm/3110e55750143a84918d7423febc9c83a55bc28c
/usr/share/package-licenses/helm/33cd8e150548e595fbe201c6ca9df582976e71db
/usr/share/package-licenses/helm/376caa2cd54c4196280157d071524614350e7ce8
/usr/share/package-licenses/helm/3faf341fbc32621fe1ac089ae2ab7a23980fc189
/usr/share/package-licenses/helm/40ed8341d216cd2b3ecacc876babb86de444b800
/usr/share/package-licenses/helm/43c02fe811dfc96363cdd8ec756ecc728ab845a9
/usr/share/package-licenses/helm/45d072ce2a777c39a639bfce7cb3c27132ea3a64
/usr/share/package-licenses/helm/51bad2bd8dc245d3cd45f69b6dd4e52f97131e6a
/usr/share/package-licenses/helm/51ed3a4a1e142924d057f46a167c1e725da33ea6
/usr/share/package-licenses/helm/535e3badf5b532d842627b504976fbb93bc2d8b8
/usr/share/package-licenses/helm/53b850c91770a865abb0838b1f0eee0476d41f97
/usr/share/package-licenses/helm/5476f2f91673ef040f1956907e7f45e72d5e11ee
/usr/share/package-licenses/helm/554fb441fbb1607579b7c9f8e9d7fab5d00e3a51
/usr/share/package-licenses/helm/555e9ac61d94352b3c2935e77b51fc6dc31d4822
/usr/share/package-licenses/helm/563519fec7769aaec054ee06cb429f39f0fdab89
/usr/share/package-licenses/helm/56b820712432e458f05f883566ca8cd85dcdaad5
/usr/share/package-licenses/helm/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
/usr/share/package-licenses/helm/5a7d7df655ba40478fae80a6abafc6afc36f9b6a
/usr/share/package-licenses/helm/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/helm/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/helm/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/helm/5cc38e91ed50df624def2d682d8e033d25917167
/usr/share/package-licenses/helm/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/helm/736c20a685418b27e6992d88c0959152991d33bf
/usr/share/package-licenses/helm/773bfa66739275c14ad854cdef4f550973fbaee6
/usr/share/package-licenses/helm/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/helm/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/helm/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/helm/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
/usr/share/package-licenses/helm/836ef1b46953afdb78ce3929bc6831ca83620b65
/usr/share/package-licenses/helm/8758b52c623c08eff9cadbd0f0e1541085e9984d
/usr/share/package-licenses/helm/878e7d86573d6c8ff65d2eaab294734b3f4d3d81
/usr/share/package-licenses/helm/87a1773b9070fa0f9d4033df28f9bcba336279b1
/usr/share/package-licenses/helm/892204393ca075d09c8b1c1d880aba1ae0a2b805
/usr/share/package-licenses/helm/8bc609022fad5f9e8aec8889ab9cb195afd5ecc5
/usr/share/package-licenses/helm/8fb92f475d78da1315877a719c6856fc64531d30
/usr/share/package-licenses/helm/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
/usr/share/package-licenses/helm/91048638b5f60b9649fdaf66d1c921f15ce5f963
/usr/share/package-licenses/helm/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/helm/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/helm/93ac97c9679b68518f1fd7de627ce2f77f44082d
/usr/share/package-licenses/helm/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/helm/979fd7d5c67073b265d96f584aac3de1c419b8e2
/usr/share/package-licenses/helm/9a06b8c36ca519c5a7c67f102bf5d03aae470fa1
/usr/share/package-licenses/helm/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/helm/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/helm/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f
/usr/share/package-licenses/helm/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/helm/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/helm/b010e169e965af2c274a7001b7e32cd77fd4fd85
/usr/share/package-licenses/helm/b0eab1611332b5c5d43728e84e6bc47569775bc0
/usr/share/package-licenses/helm/b132e03c6b6bd85fbc2394f808acae8f5d0ebaf0
/usr/share/package-licenses/helm/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
/usr/share/package-licenses/helm/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/helm/b6744ad41956605ebba2359b9cb728a7a68664d7
/usr/share/package-licenses/helm/b7173385030ef97bce57b5b4b78b48763c83aed3
/usr/share/package-licenses/helm/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
/usr/share/package-licenses/helm/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/helm/c111106ab0af1873aa6350f797759fe1519c8be1
/usr/share/package-licenses/helm/c6821d75aac4a65fae7d56a425e304beb3689c26
/usr/share/package-licenses/helm/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/helm/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/helm/c9db89ee093e8877dec1561919147d3680182146
/usr/share/package-licenses/helm/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/helm/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/helm/d3b7a70b03b43d4e7205d178100581923a0baad2
/usr/share/package-licenses/helm/d676a57141ac47c27699fc8b03e1a2e59abb96ef
/usr/share/package-licenses/helm/d67b593949431da7b7972a3517af80b377ad8598
/usr/share/package-licenses/helm/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/helm/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/helm/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
/usr/share/package-licenses/helm/e625f9555286c04d831ffbaf5b27a8668f1aa1a7
/usr/share/package-licenses/helm/ece3df1263c100f93c427face535a292723d38e7
/usr/share/package-licenses/helm/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
/usr/share/package-licenses/helm/f0524399083fa802c72bc733a5e12ed1342c650f
/usr/share/package-licenses/helm/f3eab54cb1736b419ef75b8c44bea2b17614bd31
/usr/share/package-licenses/helm/f4f6a4a62f50348c9f4fa311fd2023d8ed32e380
/usr/share/package-licenses/helm/f7f33fde14de785a3ac53f250bb746ba30844639
/usr/share/package-licenses/helm/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
/usr/share/package-licenses/helm/fd6460234f122a19f21affb6d6885269340b9176
/usr/share/package-licenses/helm/feb9285b75d0c82a47d32e7d4dc84eb02db9ee34
