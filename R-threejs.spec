#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-threejs
Version  : 0.3.1
Release  : 13
URL      : https://cran.r-project.org/src/contrib/threejs_0.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/threejs_0.3.1.tar.gz
Summary  : Interactive 3D Scatter Plots, Networks and Globes
Group    : Development/Tools
License  : MIT
Requires: R-base64enc
Requires: R-crosstalk
Requires: R-htmlwidgets
Requires: R-igraph
BuildRequires : R-base64enc
BuildRequires : R-crosstalk
BuildRequires : R-htmlwidgets
BuildRequires : R-igraph
BuildRequires : clr-R-helpers

%description
# Three.js and R
Three.js widgets for R and shiny. The package includes
* graphjs: an interactive network visualization widget
* scatterplot3js: a 3-d scatterplot widget similar to, but more limited than, the scatterplot3d function
* globejs: a somewhat silly widget that plots data and images on a 3-d globe

%prep
%setup -q -c -n threejs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521234322

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521234322
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library threejs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library threejs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library threejs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library threejs|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/threejs/DESCRIPTION
/usr/lib64/R/library/threejs/INDEX
/usr/lib64/R/library/threejs/LICENSE
/usr/lib64/R/library/threejs/Meta/Rd.rds
/usr/lib64/R/library/threejs/Meta/data.rds
/usr/lib64/R/library/threejs/Meta/demo.rds
/usr/lib64/R/library/threejs/Meta/features.rds
/usr/lib64/R/library/threejs/Meta/hsearch.rds
/usr/lib64/R/library/threejs/Meta/links.rds
/usr/lib64/R/library/threejs/Meta/nsInfo.rds
/usr/lib64/R/library/threejs/Meta/package.rds
/usr/lib64/R/library/threejs/NAMESPACE
/usr/lib64/R/library/threejs/R/threejs
/usr/lib64/R/library/threejs/R/threejs.rdb
/usr/lib64/R/library/threejs/R/threejs.rdx
/usr/lib64/R/library/threejs/data/LeMis.RData
/usr/lib64/R/library/threejs/data/ego.RData
/usr/lib64/R/library/threejs/data/flights.RData
/usr/lib64/R/library/threejs/demo/click_animation.R
/usr/lib64/R/library/threejs/demo/click_animation2.R
/usr/lib64/R/library/threejs/demo/crosstalk.R
/usr/lib64/R/library/threejs/examples/globe/server.R
/usr/lib64/R/library/threejs/examples/globe/ui.R
/usr/lib64/R/library/threejs/examples/graph/server.R
/usr/lib64/R/library/threejs/examples/graph/ui.R
/usr/lib64/R/library/threejs/examples/scatterplot/server.R
/usr/lib64/R/library/threejs/examples/scatterplot/ui.R
/usr/lib64/R/library/threejs/help/AnIndex
/usr/lib64/R/library/threejs/help/aliases.rds
/usr/lib64/R/library/threejs/help/paths.rds
/usr/lib64/R/library/threejs/help/threejs.rdb
/usr/lib64/R/library/threejs/help/threejs.rdx
/usr/lib64/R/library/threejs/html/00Index.html
/usr/lib64/R/library/threejs/html/R.css
/usr/lib64/R/library/threejs/htmlwidgets/globe.js
/usr/lib64/R/library/threejs/htmlwidgets/globe.yaml
/usr/lib64/R/library/threejs/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/threejs/htmlwidgets/lib/threejs-85/CanvasRenderer.js
/usr/lib64/R/library/threejs/htmlwidgets/lib/threejs-85/Detector.js
/usr/lib64/R/library/threejs/htmlwidgets/lib/threejs-85/Projector.js
/usr/lib64/R/library/threejs/htmlwidgets/lib/threejs-85/StateOrbitControls.js
/usr/lib64/R/library/threejs/htmlwidgets/lib/threejs-85/TrackballControls.js
/usr/lib64/R/library/threejs/htmlwidgets/lib/threejs-85/three.min.js
/usr/lib64/R/library/threejs/htmlwidgets/scatterplotThree.js
/usr/lib64/R/library/threejs/htmlwidgets/scatterplotThree.yaml
/usr/lib64/R/library/threejs/images/circle.png
/usr/lib64/R/library/threejs/images/disc.png
/usr/lib64/R/library/threejs/images/moon.jpg
/usr/lib64/R/library/threejs/images/plus.png
/usr/lib64/R/library/threejs/images/world.jpg
