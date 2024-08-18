Name:		texlive-dvips
Epoch:		1
Version:	70015
Release:	1
Summary:	A DVI to PostScript driver
Group:		Publishing
URL:		http://tug.org/texlive
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvips.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvips.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-dvips.bin
%rename tetex-dvips
%rename texlive-texmf-dvips

%description
This package has been withdrawn from CTAN, and bundled into the
distributions' package sets. The current sources of dvips may
be found in the distribution of dvipsk which forms part of the
TeX-live sources.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	rm -fr %{_texmfvardir}/fonts/map/dvips
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips
%{_texmfdistdir}/fonts/enc/dvips
%{_texmfdistdir}/tex/generic/dvips
%doc %{_texmfdistdir}/doc/dvips
%doc %{_infodir}/dvips.info*
%doc %{_mandir}/man1/afm2tfm.1*
%doc %{_texmfdistdir}/doc/man/man1/afm2tfm.man1.pdf
%doc %{_mandir}/man1/dvips.1*
%doc %{_texmfdistdir}/doc/man/man1/dvips.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
