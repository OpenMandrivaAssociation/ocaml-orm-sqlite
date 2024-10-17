%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	An "Object-Relational Mapper" interface between a Sqlite3 database and OCaml
Name:		ocaml-orm-sqlite
Version:	0.2
Release:	4
License:	ISC
Group:		Development/Other
Url:		https://wiki.github.com/avsm/ocaml-orm-sqlite
Source0:	ocaml-orm-sqlite-0.2.tar.bz2
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-sqlite-devel

%description
You provide a schema of the type of objects you want to store in the database,
and an OCaml source file is generated with modules that:

 * initialize the database with the right schema
 * retrieve objects from the database by searching from keys
 * modify fields and save them back to the database.

%files
%doc LICENSE NEWS TODO README
%dir %{_libdir}/ocaml/sql_orm
%{_libdir}/ocaml/sql_orm/META
%{_libdir}/ocaml/sql_orm/*.cma
%{_libdir}/ocaml/sql_orm/*.cmi

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE
%doc doc/ examples/ tests/
%{_libdir}/ocaml/sql_orm/*.a
%{_libdir}/ocaml/sql_orm/*.cmxa
%{_libdir}/ocaml/sql_orm/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q

%build
make all
mkdir -p doc && ocamldoc -d doc -html sql_orm.mli

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/sql_orm
make install

