Name:           ros-indigo-swri-nodelet
Version:        0.0.14
Release:        0%{?dist}
Summary:        ROS swri_nodelet package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-nodelet
Requires:       ros-indigo-rosbash
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-rosbash
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs

%description
This package provides a simple script to write simple launch files that can
easily switch between running nodelets together or as standalone nodes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Apr 11 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.0.14-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.0.13-1
- Autogenerated by Bloom

* Sun Oct 23 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.13-0
- Autogenerated by Bloom

* Sun Aug 14 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.12-0
- Autogenerated by Bloom

* Fri May 13 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.11-0
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-3
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-2
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-1
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-0
- Autogenerated by Bloom

