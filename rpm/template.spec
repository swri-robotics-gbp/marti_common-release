Name:           ros-melodic-swri-nodelet
Version:        2.5.0
Release:        0%{?dist}
Summary:        ROS swri_nodelet package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-nodelet
Requires:       ros-melodic-rosbash
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-rosbash
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-std-msgs

%description
This package provides a simple script to write simple launch files that can
easily switch between running nodelets together or as standalone nodes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Oct 12 2018 P. J. Reed <preed@swri.org> - 2.5.0-0
- Autogenerated by Bloom

* Tue Oct 09 2018 P. J. Reed <preed@swri.org> - 2.4.0-0
- Autogenerated by Bloom

* Fri May 25 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.3.0-0
- Autogenerated by Bloom

* Fri May 11 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.2.1-0
- Autogenerated by Bloom

