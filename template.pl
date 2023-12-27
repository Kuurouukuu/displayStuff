#!/usr/bin/perl
use strict;
use warnings;

my $template_file = "a_template";
my $input_file = "input2";

open(my $template_fh, '<', $template_file) or die "Could not open file '$template_file' $!";
my $template = do { local $/; <$template_fh> };
close($template_fh);

open(my $input_fh, '<', $input_file) or die "Could not open file '$input_file' $!";
my $input = do { local $/; <$input_fh> };
close($input_fh);

$template =~ s/_placeholder/$input/g;

print $template;
