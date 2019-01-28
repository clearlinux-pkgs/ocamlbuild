#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ocamlbuild
Version  : 0.13.1
Release  : 5
URL      : https://github.com/ocaml/ocamlbuild/archive/0.13.1.tar.gz
Source0  : https://github.com/ocaml/ocamlbuild/archive/0.13.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0
Requires: ocamlbuild-bin = %{version}-%{release}
Requires: ocamlbuild-license = %{version}-%{release}
Requires: ocamlbuild-man = %{version}-%{release}
BuildRequires : ocaml
BuildRequires : util-linux

%description
The organization of tests is the following:
- internal.ml contains the tests that should be runnable from a bare
OCaml installation -- always passing the -no-ocamlfind option.

%package bin
Summary: bin components for the ocamlbuild package.
Group: Binaries
Requires: ocamlbuild-license = %{version}-%{release}
Requires: ocamlbuild-man = %{version}-%{release}

%description bin
bin components for the ocamlbuild package.


%package license
Summary: license components for the ocamlbuild package.
Group: Default

%description license
license components for the ocamlbuild package.


%package man
Summary: man components for the ocamlbuild package.
Group: Default

%description man
man components for the ocamlbuild package.


%prep
%setup -q -n ocamlbuild-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548706148
## make_prepend content
make configure
## make_prepend end
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1548706148
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ocamlbuild
cp LICENSE %{buildroot}/usr/share/package-licenses/ocamlbuild/LICENSE
cp manual/LICENSE %{buildroot}/usr/share/package-licenses/ocamlbuild/manual_LICENSE
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/ocaml/ocamlbuild/META
/usr/lib64/ocaml/ocamlbuild/ocamlbuild.cmo
/usr/lib64/ocaml/ocamlbuild/ocamlbuild.cmx
/usr/lib64/ocaml/ocamlbuild/ocamlbuild.o
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_executor.cmi
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_executor.cmx
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_executor.o
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_pack.cmi
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_pack.cmx
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_plugin.cmi
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_plugin.cmx
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_plugin.o
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_unix_plugin.cmi
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_unix_plugin.cmx
/usr/lib64/ocaml/ocamlbuild/ocamlbuild_unix_plugin.o
/usr/lib64/ocaml/ocamlbuild/ocamlbuildlib.cma
/usr/lib64/ocaml/ocamlbuild/ocamlbuildlib.cmxa
/usr/lib64/ocaml/ocamlbuild/signatures.cmi
/usr/lib64/ocaml/ocamlbuild/signatures.cmti
/usr/lib64/ocaml/ocamlbuild/signatures.mli

%files bin
%defattr(-,root,root,-)
/usr/bin/ocamlbuild
/usr/bin/ocamlbuild.byte
/usr/bin/ocamlbuild.native

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ocamlbuild/LICENSE
/usr/share/package-licenses/ocamlbuild/manual_LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ocamlbuild.1
