# revision 27932
# category Package
# catalog-ctan undef
# catalog-date 2012-07-03 17:35:36 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-dvips
Version:	20120703
Release:	2
Summary:	A DVI to PostScript driver
Group:		Publishing
URL:		http://tug.org/texlive
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvips.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvips.doc.tar.xz
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
%{_texmfdistdir}/dvips/base/ehandler.ps
%{_texmfdistdir}/dvips/base/resolution400.ps
%{_texmfdistdir}/fonts/enc/dvips/base/6w.enc
%{_texmfdistdir}/fonts/enc/dvips/base/7t.enc
%{_texmfdistdir}/fonts/enc/dvips/base/8a.enc
%{_texmfdistdir}/fonts/enc/dvips/base/8r.enc
%{_texmfdistdir}/fonts/enc/dvips/base/ad.enc
%{_texmfdistdir}/fonts/enc/dvips/base/ansinew.enc
%{_texmfdistdir}/fonts/enc/dvips/base/asex.enc
%{_texmfdistdir}/fonts/enc/dvips/base/asexp.enc
%{_texmfdistdir}/fonts/enc/dvips/base/dc.enc
%{_texmfdistdir}/fonts/enc/dvips/base/dvips.enc
%{_texmfdistdir}/fonts/enc/dvips/base/ec.enc
%{_texmfdistdir}/fonts/enc/dvips/base/extex.enc
%{_texmfdistdir}/fonts/enc/dvips/base/funky.enc
%{_texmfdistdir}/fonts/enc/dvips/base/odvips.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-cs-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-ec-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-l7x-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-qx-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-rm-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-t2a-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-t2b-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-t2c-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-t5-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-texnansi-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/q-ts1-uni.enc
%{_texmfdistdir}/fonts/enc/dvips/base/qx.enc
%{_texmfdistdir}/fonts/enc/dvips/base/stormex.enc
%{_texmfdistdir}/fonts/enc/dvips/base/tex256.enc
%{_texmfdistdir}/fonts/enc/dvips/base/texmext.enc
%{_texmfdistdir}/fonts/enc/dvips/base/texmital.enc
%{_texmfdistdir}/fonts/enc/dvips/base/texmsym.enc
%{_texmfdistdir}/fonts/enc/dvips/base/texnansx.enc
%{_texmfdistdir}/fonts/enc/dvips/base/xl2.enc
%{_texmfdistdir}/fonts/enc/dvips/base/xt2.enc
%{_texmfdistdir}/tex/generic/dvips/blackdvi.sty
%{_texmfdistdir}/tex/generic/dvips/blackdvi.tex
%{_texmfdistdir}/tex/generic/dvips/colordvi.sty
%{_texmfdistdir}/tex/generic/dvips/colordvi.tex
%{_texmfdistdir}/tex/generic/dvips/rotate.sty
%{_texmfdistdir}/tex/generic/dvips/rotate.tex
%{_texmfdir}/dvips/base/color.pro
%{_texmfdir}/dvips/base/crop.pro
%{_texmfdir}/dvips/base/finclude.pro
%{_texmfdir}/dvips/base/hps.pro
%{_texmfdir}/dvips/base/special.pro
%{_texmfdir}/dvips/base/tex.pro
%{_texmfdir}/dvips/base/texc.pro
%{_texmfdir}/dvips/base/texps.pro
%{_texmfdir}/dvips/config/alt-rule.pro
%{_texmfdir}/dvips/config/canonex.cfg
%{_texmfdir}/dvips/config/config.bakoma
%{_texmfdir}/dvips/config/config.canonex
%{_texmfdir}/dvips/config/config.cx
%{_texmfdir}/dvips/config/config.deskjet
%{_texmfdir}/dvips/config/config.dvired
%{_texmfdir}/dvips/config/config.epson
%{_texmfdir}/dvips/config/config.ibmvga
%{_texmfdir}/dvips/config/config.ljfour
%{_texmfdir}/dvips/config/config.luc
%{_texmfdir}/dvips/config/config.mbn
%{_texmfdir}/dvips/config/config.mga
%{_texmfdir}/dvips/config/config.mirrorprint
%{_texmfdir}/dvips/config/config.ot2
%{_texmfdir}/dvips/config/config.ps
%{_texmfdir}/dvips/config/config.qms
%{_texmfdir}/dvips/config/config.toshiba
%{_texmfdir}/dvips/config/config.unms
%{_texmfdir}/dvips/config/config.xyp
%{_texmfdir}/dvips/config/cx.cfg
%{_texmfdir}/dvips/config/deskjet.cfg
%{_texmfdir}/dvips/config/dfaxhigh.cfg
%{_texmfdir}/dvips/config/dvired.cfg
%{_texmfdir}/dvips/config/epson.cfg
%{_texmfdir}/dvips/config/ibmvga.cfg
%{_texmfdir}/dvips/config/ljfour.cfg
%{_texmfdir}/dvips/config/qms.cfg
%{_texmfdir}/dvips/config/toshiba.cfg
%{_texmfdir}/fonts/map/dvips/updmap/builtin35.map
%{_texmfdir}/fonts/map/dvips/updmap/download35.map
%{_texmfdir}/fonts/map/dvips/updmap/ps2pk.map
%{_texmfdir}/fonts/map/dvips/updmap/psfonts.map
%{_texmfdir}/fonts/map/dvips/updmap/psfonts_pk.map
%{_texmfdir}/fonts/map/dvips/updmap/psfonts_t1.map
%doc %{_texmfdir}/doc/dvips/dvips.html
%doc %{_texmfdir}/doc/dvips/dvips.pdf
%doc %{_infodir}/dvips.info*
%doc %{_mandir}/man1/afm2tfm.1*
%doc %{_texmfdir}/doc/man/man1/afm2tfm.man1.pdf
%doc %{_mandir}/man1/dvips.1*
%doc %{_texmfdir}/doc/man/man1/dvips.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdir}/doc/info/*.info %{buildroot}%{_infodir}
