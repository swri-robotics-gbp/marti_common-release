Name:           ros-melodic-swri-image-util
Version:        2.7.0
Release:        0%{?dist}
Summary:        ROS swri_image_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-melodic-camera-calibration-parsers
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-image-geometry
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-message-filters
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-swri-geometry-util
Requires:       ros-melodic-swri-math-util
Requires:       ros-melodic-swri-opencv-util
Requires:       ros-melodic-swri-roscpp
Requires:       ros-melodic-tf
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-melodic-camera-calibration-parsers
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-image-geometry
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-swri-geometry-util
BuildRequires:  ros-melodic-swri-math-util
BuildRequires:  ros-melodic-swri-nodelet
BuildRequires:  ros-melodic-swri-opencv-util
BuildRequires:  ros-melodic-swri-roscpp
BuildRequires:  ros-melodic-tf

%description
swri_image_util

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
* Tue Dec 04 2018 Kris Kozak <kkozak@swri.org> - 2.7.0-0
- Autogenerated by Bloom

* Sat Nov 03 2018 Kris Kozak <kkozak@swri.org> - 2.6.0-0
- Autogenerated by Bloom

* Fri Oct 12 2018 Kris Kozak <kkozak@swri.org> - 2.5.0-0
- Autogenerated by Bloom

* Tue Oct 09 2018 Kris Kozak <kkozak@swri.org> - 2.4.0-0
- Autogenerated by Bloom

* Fri May 25 2018 Kris Kozak <kkozak@swri.org> - 2.3.0-0
- Autogenerated by Bloom

* Fri May 11 2018 Kris Kozak <kkozak@swri.org> - 2.2.1-0
- Autogenerated by Bloom

