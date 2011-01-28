#
%define	wx_config	wx-gtk2-ansi-config
%define	wx_major	%(%{wx_config} --version | cut -d. -f1)
%define	wx_minor	%(%{wx_config} --version | cut -d. -f2)
#
Summary:	A property sheet control for wxWidgets
Summary(pl.UTF-8):	Widget dla wxWidgets stworzony do edycji właściwości obiektów
Name:		wxpropgrid
Version:	1.4.1
Release:	1
License:	wxWindows License
Group:		Libraries
Source0:	http://downloads.sourceforge.net/wxpropgrid/%{name}-%{version}-src.tar.gz
# Source0-md5:	15f76092c2b84cca8ebf1577cd9a0bc6
Patch0:		%{name}-no-sample.patch
URL:		http://wxpropgrid.sourceforge.net/
BuildRequires:	wxGTK2-devel >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxPropertyGrid is a property sheet control for wxWidgets. In other
words, it is a specialized two-column grid for editing properties such
as strings, numbers, flagsets, string arrays, and colours.

%description -l pl.UTF-8
wxPropetyGrid jest widgetem do edycji właściwości obiektów.
Innymisłowy jest to dwu kolumnowa tablica, pozwalająca konfigirować
ciągi znaków, liczby, flagi, tablice i kolory dla poszczególnych
wierszy.

%package devel
Summary:	Header files for wxPropertyGrid library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxPropetyGrid
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for wxPropetyGrid library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wxPropetyGrid.

%prep
%setup -qn propgrid
%patch0 -p1

%build
cd build && %{__make} -f GNUMakefile	\
	prefix="%{_prefix}"		\
	CC="%{__cc}"			\
	CXX="%{__cxx}"			\
	CFLAGS="%{rpmcflags}"		\
	CXXFLAGS="%{rpmcxxflags}"	\
	LDFLAGS="%{rpmldflags}"		\
	WX_CONFIG=%{wx_config}		\
	WX_VERSION_MAJOR=%{wx_major}	\
	WX_VERSION_MINOR=%{wx_minor}

%install
rm -rf $RPM_BUILD_ROOT

cd build && %{__make} -f GNUMakefile	\
	prefix="%{_prefix}"		\
	CC="%{__cc}"			\
	CXX="%{__cxx}"			\
	CFLAGS="%{rpmcflags}"		\
	CXXFLAGS="%{rpmcxxflags}"	\
	LDFLAGS="%{rpmldflags}"		\
	WX_CONFIG=%{wx_config}		\
	WX_VERSION_MAJOR=%{wx_major}	\
	WX_VERSION_MINOR=%{wx_minor}	\
	DESTDIR=$RPM_BUILD_ROOT		\
	install

[ %{_libdir} != %{_prefix}/lib ] &&	\
	mv $RPM_BUILD_ROOT%{_prefix}/lib $RPM_BUILD_ROOT%{_libdir}

install -d $RPM_BUILD_ROOT%{_includedir}/wx-%{wx_major}.%{wx_minor}
mv $RPM_BUILD_ROOT%{_includedir}/wx	\
	$RPM_BUILD_ROOT%{_includedir}/wx-%{wx_major}.%{wx_minor}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%{_includedir}/wx-%{wx_major}.%{wx_minor}/wx/propgrid
