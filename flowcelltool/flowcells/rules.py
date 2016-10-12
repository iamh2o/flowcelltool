# -*- coding: utf-8 -*-
import rules

INSTRUMENT_OPERATOR = 'Instrument Operator'
DEMUX_OPERATOR = 'Demultiplexing Operator'
DEMUX_ADMIN = 'Demultiplexing Admin'
IMPORT_BOT = 'Import Bot'

# Predicates ------------------------------------------------------------------


@rules.predicate
def is_flow_cell_owner(user, flow_cell):
    """Whether or not user is owner of the given flow cell"""
    if not flow_cell:
        return False
    else:
        return flow_cell.owner == user


@rules.predicate
def is_librarys_flow_cell_owner(user, library):
    """Whether or not is owner of the given flow cell's library'"""
    if not library or not library.flow_cell:
        return False
    else:
        return library.flow_cell.owner == user


#: Whether or not has the "Instrument Operator" group
is_instrument_operator = rules.is_group_member(INSTRUMENT_OPERATOR)

#: Whether or not has the "Demultiplexing Operator" group
is_demux_operator = rules.is_group_member(DEMUX_OPERATOR)

#: Whether or not has the "Demultiplexing Admin" group
is_demux_admin = rules.is_group_member(DEMUX_ADMIN)

#: Whether or not has the "Import Bot" group
is_import_bot = rules.is_group_member(IMPORT_BOT)


# Rules -----------------------------------------------------------------------

# TODO: I don't see what I need rules for if I have permissions...

# Permissions -----------------------------------------------------------------

# Allow everyone access to flow cells
rules.add_perm('flowcells', rules.always_allow)

# Adding and updating sequencing machines requires to be a demultiplexing
# administrator as this can be very destructive
rules.add_perm('flowcells.add_sequencingmachine',
               is_demux_admin | rules.is_superuser)
rules.add_perm('flowcells.change_sequencingmachine',
               is_demux_admin | rules.is_superuser)
rules.add_perm('flowcells.delete_sequencingmachine',
               is_demux_admin | rules.is_superuser)

# Adding and updating barcode sets requires to be a demultiplexing
# administrator as this can be very destructive
rules.add_perm('flowcells.add_barcodeset',
               is_demux_admin | rules.is_superuser)
rules.add_perm('flowcells.change_barcodeset',
               is_demux_admin | rules.is_superuser)
rules.add_perm('flowcells.delete_barcodeset',
               is_demux_admin | rules.is_superuser)

# Adding and updating barcode set entries requires to be a demultiplexing
# administrator as this can be very destructive
rules.add_perm('flowcells.add_barcodesetentry',
               is_demux_admin | rules.is_superuser)
rules.add_perm('flowcells.change_barcodesetentry',
               is_demux_admin | rules.is_superuser)
rules.add_perm('flowcells.delete_barcodesetentry',
               is_demux_admin | rules.is_superuser)

# Adding flow cells can be done by everyone, updating is only possible to
# owners, demux operators and upwards.
rules.add_perm(
    'flowcells.add_flowcell',
    is_instrument_operator | is_demux_operator | is_demux_admin
    | is_import_bot | rules.is_superuser
)
rules.add_perm(
    'flowcells.change_flowcell',
    is_flow_cell_owner | is_demux_operator | is_demux_admin | is_import_bot
    | rules.is_superuser
)
rules.add_perm(
    'flowcells.delete_flowcell',
    is_demux_operator | is_demux_admin | is_import_bot | rules.is_superuser
)

# Similar, for library on flowcell
rules.add_perm(
    'flowcells.add_library',
    is_librarys_flow_cell_owner | is_demux_operator | is_demux_admin
    | is_import_bot | rules.is_superuser
)
rules.add_perm(
    'flowcells.change_library',
    is_librarys_flow_cell_owner | is_demux_operator | is_demux_admin
    | is_import_bot | rules.is_superuser
)
rules.add_perm(
    'flowcells.delete_library',
    is_librarys_flow_cell_owner | is_demux_admin
    | is_import_bot | rules.is_superuser
)