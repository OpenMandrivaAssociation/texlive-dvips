%global tl_name dvips
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A DVI to PostScript driver
Group:		Publishing
URL:		https://www.ctan.org/pkg/dvips
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvips.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvips.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dvips.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package has been withdrawn from CTAN, and bundled into the
distributions' package sets. Development now takes place within the TeX
Live framework, and it is no longer available as a separate package. For
download, support, and other information, please see TeX Live.

