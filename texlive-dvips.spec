# revision 32132
# category Package
# catalog-ctan undef
# catalog-date 2013-03-25 12:41:24 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-dvips
Version:	20130325
Release:	3
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
%{_texmfdistdir}/dvips/base/color.pro
%{_texmfdistdir}/dvips/base/crop.pro
%{_texmfdistdir}/dvips/base/ehandler.ps
%{_texmfdistdir}/dvips/base/finclude.pro
%{_texmfdistdir}/dvips/base/hps.pro
%{_texmfdistdir}/dvips/base/resolution400.ps
%{_texmfdistdir}/dvips/base/special.pro
%{_texmfdistdir}/dvips/base/tex.pro
%{_texmfdistdir}/dvips/base/texc.pro
%{_texmfdistdir}/dvips/base/texps.pro
%{_texmfdistdir}/dvips/config/alt-rule.pro
%{_texmfdistdir}/dvips/config/canonex.cfg
%{_texmfdistdir}/dvips/config/config.bakoma
%{_texmfdistdir}/dvips/config/config.canonex
%{_texmfdistdir}/dvips/config/config.cx
%{_texmfdistdir}/dvips/config/config.deskjet
%{_texmfdistdir}/dvips/config/config.dvired
%{_texmfdistdir}/dvips/config/config.epson
%{_texmfdistdir}/dvips/config/config.ibmvga
%{_texmfdistdir}/dvips/config/config.ljfour
%{_texmfdistdir}/dvips/config/config.luc
%{_texmfdistdir}/dvips/config/config.mbn
%{_texmfdistdir}/dvips/config/config.mga
%{_texmfdistdir}/dvips/config/config.mirrorprint
%{_texmfdistdir}/dvips/config/config.ot2
%{_texmfdistdir}/dvips/config/config.ps
%{_texmfdistdir}/dvips/config/config.qms
%{_texmfdistdir}/dvips/config/config.toshiba
%{_texmfdistdir}/dvips/config/config.unms
%{_texmfdistdir}/dvips/config/config.xyp
%{_texmfdistdir}/dvips/config/cx.cfg
%{_texmfdistdir}/dvips/config/deskjet.cfg
%{_texmfdistdir}/dvips/config/dfaxhigh.cfg
%{_texmfdistdir}/dvips/config/dvired.cfg
%{_texmfdistdir}/dvips/config/epson.cfg
%{_texmfdistdir}/dvips/config/ibmvga.cfg
%{_texmfdistdir}/dvips/config/ljfour.cfg
%{_texmfdistdir}/dvips/config/qms.cfg
%{_texmfdistdir}/dvips/config/toshiba.cfg
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
%{_texmfdistdir}/fonts/map/dvips/updmap/builtin35.map
%{_texmfdistdir}/fonts/map/dvips/updmap/download35.map
%{_texmfdistdir}/fonts/map/dvips/updmap/ps2pk.map
%{_texmfdistdir}/fonts/map/dvips/updmap/psfonts.map
%{_texmfdistdir}/fonts/map/dvips/updmap/psfonts_pk.map
%{_texmfdistdir}/fonts/map/dvips/updmap/psfonts_t1.map
%{_texmfdistdir}/tex/generic/dvips/blackdvi.sty
%{_texmfdistdir}/tex/generic/dvips/blackdvi.tex
%{_texmfdistdir}/tex/generic/dvips/colordvi.sty
%{_texmfdistdir}/tex/generic/dvips/colordvi.tex
%{_texmfdistdir}/tex/generic/dvips/rotate.sty
%{_texmfdistdir}/tex/generic/dvips/rotate.tex
%doc %{_texmfdistdir}/doc/dvips/dvips.html
%doc %{_texmfdistdir}/doc/dvips/dvips.pdf
%doc %{_infodir}/dvips.info*
%doc %{_mandir}/man1/afm2tfm.1*
%doc %{_texmfdistdir}/doc/man/man1/afm2tfm.man1.pdf
%doc %{_mandir}/man1/dvips.1*
%doc %{_texmfdistdir}/doc/man/man1/dvips.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
